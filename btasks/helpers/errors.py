from flask import jsonify


def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return jsonify({'error': 'Internal error', 'detail': str(e)}), 500

    @app.errorhandler(Exception)
    def base_error_handler(e):
        return jsonify({'error': 'Internal error', 'detail': str(e)}), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return jsonify({'error': 'Resource not found', 'detail': str(e)}), 404

    @app.errorhandler(401)
    def error_401_handler(e):
        return jsonify({'error': 'Unauthorized access', 'detail': str(e)}), 401
