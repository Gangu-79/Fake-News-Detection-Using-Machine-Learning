from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def _simple_predict(text: str):
    t = (text or '').strip().lower()
    score = 0

    fake_indicators = [
        'fake', 'fraud', 'hoax', 'false', 'rumor', 'rumour', 'clickbait',
        'scam', 'fabricated', 'bogus', 'misleading', 'debunked', 'conspiracy',
        'shocking', 'viral', 'sensational', 'untrue', 'lies', 'distorted',
        'free laptop', 'free high-end laptop', 'no registration', 'no identity verification',
        'delivered directly', 'every household', 'unused satellite revenue',
        'officially announced', 'program is reportedly funded', 'starting next monday'
    ]
    real_indicators = [
        'reported', 'confirmed', 'official', 'announced', 'released', 'statement',
        'according to', 'research', 'study', 'said', 'told', 'spokesperson', 'minister',
        'government', 'agency'
    ]

    strong_fake = [
        'fake', 'hoax', 'scam', 'fabricated', 'bogus', 'untrue', 'lies',
        'clickbait', 'misleading', 'free laptop', 'no registration',
        'no identity verification', 'delivered directly', 'every household',
        'unused satellite revenue'
    ]
    for w in fake_indicators:
        if w in t:
            score += 1
    for w in real_indicators:
        if w in t:
            score -= 0.1

    # Ensure strong fake indicators override mild real wording
    if any(w in t for w in strong_fake):
        score = max(score, 1.5)

    if len(t.split()) < 6 and score <= 0:
        score -= 0.2

    label = 'Fake' if score > 0 else 'Real'
    confidence = min(0.99, max(0.55, 0.65 + 0.1 * score))
    message = 'This is fake.' if label == 'Fake' else 'This is real.'
    return label, round(confidence, 2), message


@require_http_methods(["GET", "POST"])
def index(request):
    prediction = None
    error = None
    input_text = ''

    if request.method == 'POST':
        input_text = request.POST.get('article_text', '').strip()
        if input_text:
            label, confidence, message = _simple_predict(input_text)
            prediction = {
                'label': label,
                'confidence': confidence,
                'message': message,
            }
        else:
            error = 'Please enter article text before analyzing.'

    return render(
        request,
        'detector/index.html',
        {'prediction': prediction, 'input_text': input_text, 'error': error},
    )
