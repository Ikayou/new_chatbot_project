from django.http import JsonResponse
from django.shortcuts import render


def chatbot_response(request):
    if request.method == "POST":
        user_message = request.POST.get('message', '').lower()

        # シンプルな応答ロジック
        responses = {
            "hello": "Hi there! How can I help you?",
            "how are you?": "I'm just a bot, but I'm doing great!",
            "i am tired today": "I'm sorry to hear that. Maybe you should take a break.",
            "what is aubex gmbh?": "Aubex GmbH is a software development company.",
            "where is yuichiro from?": "He is from Japan.",
            "bye": "Goodbye! Have a nice day!",
            "thanks": "You're welcome!",
            "which car do you like?": "I like Toyota cars.",
        }

        bot_response = responses.get(user_message, "Sorry, I didn't understand that.")
        return JsonResponse({"response": bot_response})

    return render(request, 'chatbot/chat.html')
