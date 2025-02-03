from app import Server


if __name__ == "__main__":
    server = Server()
    server.get_routes()
    app = server.get_app()
    app.run(debug=True)