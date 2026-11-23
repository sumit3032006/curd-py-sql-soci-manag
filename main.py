from controller.SocietyController import run_app


if __name__ == "__main__":
    try:
        run_app()
    except KeyboardInterrupt:
        print("\nExiting program. Goodbye!")
