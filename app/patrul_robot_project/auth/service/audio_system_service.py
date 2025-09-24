from auth.dao.audio_system_dao import AudioSystemDAO

class AudioSystemService:
    @staticmethod
    def add_audio_system(has_speaker, has_microphone, has_panic_button, robot_id):
        return AudioSystemDAO.add_audio_system(has_speaker, has_microphone, has_panic_button, robot_id)

    @staticmethod
    def get_audio_system(audio_system_id):
        return AudioSystemDAO.get_audio_system(audio_system_id)

    @staticmethod
    def get_all_audio_systems():
        return AudioSystemDAO.get_all_audio_systems()

    @staticmethod
    def update_audio_system(audio_system_id, has_speaker, has_microphone, has_panic_button, robot_id):
        return AudioSystemDAO.update_audio_system(audio_system_id, has_speaker, has_microphone, has_panic_button, robot_id)

    @staticmethod
    def delete_audio_system(audio_system_id):
        return AudioSystemDAO.delete_audio_system(audio_system_id)
