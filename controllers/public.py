from app.views.public import PublicView

class PublicController:
  @staticmethod
  def public() -> str:
    message = 'Public page'
    return PublicView.public(message)