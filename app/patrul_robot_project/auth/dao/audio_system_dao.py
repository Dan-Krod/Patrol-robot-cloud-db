from auth.domain.models import db
from auth.domain.audio_system import AudioSystem

class AudioSystemDAO:
    @staticmethod
    def add_audio_system(has_speaker, has_microphone, has_panic_button, robot_id):
        new_audio_system = AudioSystem(has_speaker=has_speaker, has_microphone=has_microphone, has_panic_button=has_panic_button, robot_id=robot_id)
        db.session.add(new_audio_system)
        db.session.commit()
        return new_audio_system

    @staticmethod
    def get_audio_system(audio_system_id):
        return AudioSystem.query.get(audio_system_id)

    @staticmethod
    def get_all_audio_systems():
        return AudioSystem.query.all()

    @staticmethod
    def update_audio_system(audio_system_id, has_speaker, has_microphone, has_panic_button, robot_id):
        audio_system = AudioSystem.query.get(audio_system_id)
        if audio_system:
            audio_system.has_speaker = has_speaker
            audio_system.has_microphone = has_microphone
            audio_system.has_panic_button = has_panic_button
            audio_system.robot_id = robot_id
            db.session.commit()
        return audio_system

    @staticmethod
    def delete_audio_system(audio_system_id):
        audio_system = AudioSystem.query.get(audio_system_id)
        if audio_system:
            db.session.delete(audio_system)
            db.session.commit()
        return audio_system
