from app.views.protected import ProtectedView

class ProtectedController:
    @staticmethod
    def protected_page() -> str:
        msg = 'Protected page'
        return ProtectedView.protected(msg)