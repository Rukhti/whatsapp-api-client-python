import unittest
from unittest.mock import patch, Mock

from whatsapp_api_client_python.API import GreenApi

api = GreenApi("", "")


class MethodsTestCase(unittest.TestCase):
    @patch("whatsapp_api_client_python.API.requests.request")
    def test_methods(self, mock_request):
        mock_request.return_value = Mock(
            status_code=200, text="{\"example\": {\"key\": \"value\"}}"
        )

        methods = [
            *self.account_methods,
            *self.device_methods,
            *self.group_methods,
            *self.log_methods,
            *self.queue_methods,
            *self.read_mark_methods,
            *self.receiving_methods,
            *self.sending_methods,
            *self.service_methods
        ]

        for response in methods:
            self.assertEqual(response.code, 200)
            self.assertEqual(response.data, {"example": {"key": "value"}})

        self.assertEqual(mock_request.call_count, len(methods))

    @property
    def account_methods(self):
        return [
            api.account.getSettings(),
            api.account.setSettings({}),
            api.account.getStateInstance(),
            api.account.getStatusInstance(),
            api.account.reboot(),
            api.account.logout(),
            api.account.qr(),
            # api.account.setProfilePicture("")
        ]

    @property
    def device_methods(self):
        return [api.device.getDeviceInfo()]

    @property
    def group_methods(self):
        return [
            api.groups.createGroup("", []),
            api.groups.updateGroupName("", ""),
            api.groups.getGroupData(""),
            api.groups.addGroupParticipant("", ""),
            api.groups.removeGroupParticipant("", ""),
            api.groups.setGroupAdmin("", ""),
            api.groups.removeAdmin("", ""),
            # api.groups.setGroupPicture("", ""),
            api.groups.leaveGroup("")
        ]

    @property
    def log_methods(self):
        return [
            api.journals.getChatHistory(""),
            api.journals.getMessage("", ""),
            api.journals.lastIncomingMessages(),
            api.journals.lastOutgoingMessages()
        ]

    @property
    def queue_methods(self):
        return [
            api.queues.showMessagesQueue(),
            api.queues.clearMessagesQueue()
        ]

    @property
    def read_mark_methods(self):
        return [api.marking.readChat("", "")]

    @property
    def receiving_methods(self):
        return [
            api.receiving.receiveNotification(),
            api.receiving.deleteNotification(0),
            api.receiving.downloadFile("")
        ]

    @property
    def sending_methods(self):
        return [
            api.sending.sendMessage("", ""),
            api.sending.sendButtons("", "", []),
            api.sending.sendTemplateButtons("", "", []),
            api.sending.sendListMessage("", "", "", []),
            # api.sending.sendFileByUpload("", ""),
            api.sending.sendFileByUrl("", "", ""),
            api.sending.sendLocation("", 0.0, 0.0),
            api.sending.sendContact("", {}),
            api.sending.sendLink("", ""),
            api.sending.forwardMessages("", "", [])
        ]

    @property
    def service_methods(self):
        return [
            api.serviceMethods.checkWhatsapp(0),
            api.serviceMethods.getAvatar(""),
            api.serviceMethods.getContacts(),
            api.serviceMethods.getContactInfo(""),
            api.serviceMethods.deleteMessage("", ""),
            api.serviceMethods.archiveChat(""),
            api.serviceMethods.unarchiveChat(""),
            api.serviceMethods.setDisappearingChat("", 0)
        ]


if __name__ == '__main__':
    unittest.main()
