import random

# Diccionario de palabras clave y respuestas
RESPUESTAS = {
    "saludos": {
        "keywords": ["hola", "buenas", "saludos", "hey", "holi"],
        "respuestas": [
            "\u00a1Hola!",
            "Hola, \u00bfcomo estas?",
            "\u00a1Saludos!"
        ]
    },
    "insultos": {
        "keywords": ["tonto", "idiota", "estupido", "imbecil"],
        "respuestas": [
            "Que grosero eres.",
            "Eso no es muy amable que digamos.",
            "Vaya, parece que alguien se desperto de mal humor."
        ]
    },
    "perdon": {
        "keywords": ["perdon", "lo siento", "disculpa"],
        "respuestas": [
            "No pasa nada, sigamos hablando.",
            "Te perdono, tranqu\u00edlo.",
            "Esta bien, no hay problema."
        ]
    },
    "pregunta": {
        "keywords": ["?"],
        "respuestas": [
            "Eso es una buena pregunta.",
            "No estoy seguro, \u00bftu que opinas?",
            "Tal vez, nunca se sabe."
        ]
    },
}



def obtener_respuesta(mensaje: str) -> str:
    """Devuelve una respuesta seg\u00fan el mensaje del usuario."""
    mensaje = mensaje.lower()

    # Revisar cada categoria en el diccionario
    for categoria, datos in RESPUESTAS.items():
        if any(palabra in mensaje for palabra in datos["keywords"]):
            return random.choice(datos["respuestas"])

    # Si no coincidio nada, devolver una respuesta por defecto
    return "No entendi eso, \u00bfme lo repites?"



def ciclo_principal():
    """Ciclo para interactuar con el bot en consola."""
    print("Escribe 'salir' para terminar la conversacion.")
    while True:
        usuario = input("Tu: ")
        if usuario.lower().strip() == "salir":
            print("Bot: Hasta luego!")
            break
        respuesta = obtener_respuesta(usuario)
        print(f"Bot: {respuesta}")


if __name__ == "__main__":
    ciclo_principal()
