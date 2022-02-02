import pygame

class SoundManager:
    @staticmethod
    def InitSound():
        pygame.init()

        pygame.mixer.music.load(_SongsMusics.main_music)

        _SongsMusics.som_laser = pygame.mixer.Sound(_SongsMusics.som_laser)
        _SongsMusics.som_invader_kill = pygame.mixer.Sound(_SongsMusics.som_invader_kill)
    
    @staticmethod
    def PlayMusic():
        pygame.mixer.music.play(-1)
    
    @staticmethod
    def StopMusic():
        pygame.mixer.music.stop()
    
    @staticmethod
    def PlayLaserSong():
        _SongsMusics.som_laser.play()

    @staticmethod
    def PlayInvaderKillSong():
        _SongsMusics.som_invader_kill.play()

class _SongsMusics:
    # Arquivos
    main_music = 'assets/sounds/music.wav'
    som_laser = 'assets/sounds/shoot.wav'
    som_invader_kill = 'assets/sounds/invaderkilled.wav'

    # Sons
    _som_laser = None
    _som_invader_kill = None