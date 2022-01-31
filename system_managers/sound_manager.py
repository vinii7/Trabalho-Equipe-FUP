import os
import pygame

class SoundManager:
    _som_laser = None
    _som_invader_kill = None

    def InitSound(self):
        music_song_path = 'assets/sounds/music.wav'
        laser_song_path = os.path.join('assets/sounds/shoot.wav')
        invader_song_path = os.path.join('assets/sounds/invaderkilled.wav')

        pygame.init()
        pygame.mixer.music.load(music_song_path)
        pygame.mixer.music.set_volume(0.05)

        # Sons
        self._som_laser = pygame.mixer.Sound(laser_song_path)
        self._som_invader_kill = pygame.mixer.Sound(invader_song_path)
    
    def PlayMusic(self):
        pygame.mixer.music.play(-1)
    
    def StopMusic(self):
        pygame.mixer.music.stop()
    
    def PlayLaserSong(self):
        self._som_laser.play()
        self._som_laser.set_volume(0.1)

    def PlayInvaderKillSong(self):
        self._som_invader_kill.play()
        self._som_invader_kill.set_volume(0.1)