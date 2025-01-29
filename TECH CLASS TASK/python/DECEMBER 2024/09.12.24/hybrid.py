class EventDetails:
    def __init__(self, event_name, event_date, event_location):
        self.event_name = event_name
        self.event_date = event_date
        self.event_location = event_location
    def display_event_details(self):
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Event Location: {self.event_location}")
class ParticipantDetails:
    def __init__(self, participant_name, participant_rollno, participant_dep):
        self.participant_name = participant_name
        self.participant_rollno = participant_rollno
        self.participant_dep = participant_dep
    def display_participant_details(self):
        print(f"Participant Name: {self.participant_name}")
        print(f"Participant RollNo: {self.participant_rollno}")
        print(f"Participant Depatment: {self.participant_dep}")
class Confirmation(EventDetails, ParticipantDetails):
    def __init__(self, event_name, event_date, event_location,
                 participant_name, participant_rollno, participant_dep):
        EventDetails.__init__(self, event_name, event_date, event_location)
        ParticipantDetails.__init__(self, participant_name, participant_rollno, participant_dep)

    def confirm_registration(self):
        print("\nConfirmation Details:")
        self.display_event_details()
        self.display_participant_details()
        print("Dear Participant,Your Registration Has Been Confirmed")
obj=Confirmation("SOLO YOGA","25.12.2024","TAMIL NADU SPORTS UNIVERSITY","KRISH","270823","DEPARTMENT OF YOGA")
obj.confirm_registration()
