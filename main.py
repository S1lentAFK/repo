from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from plyer import notification
from jnius import autoclass

class OverlayApp(App):
    def build(self):
        # Set up layout and button
        layout = FloatLayout()
        button = Button(
            text="Overlay Button",
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        button.bind(on_release=self.show_notification)
        layout.add_widget(button)
        return layout

    def show_notification(self, instance):
        # Send notification
        notification.notify(
            title="Button Clicked",
            message="You clicked the overlay button!",
        )

        # Keep this step to request SYSTEM_ALERT_WINDOW permission
        self.request_overlay_permission()

    def request_overlay_permission(self):
        # Use Java API to request overlay permission
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        Settings = autoclass('android.provider.Settings')
        Intent = autoclass('android.content.Intent')
        if not Settings.canDrawOverlays(activity):
            intent = Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION)
            activity.startActivity(intent)

if __name__ == '__main__':
    OverlayApp().run()
