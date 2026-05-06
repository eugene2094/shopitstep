from google import genai

client = genai.Client(api_key="AIzaSyA3xVuwff0eEd6ZAHVt9RTZhIVLzJwbDmQ")

def generate_ai_description(product_title):
    prompt = f"""
    Напиши продаючий опис товару українською мовою.
    Назва товару: {product_title}
    2-3 речення для інтернет-магазину.
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
    )

    return response.text
