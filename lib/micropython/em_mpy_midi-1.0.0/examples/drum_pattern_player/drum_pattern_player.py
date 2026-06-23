import time
import urandom
from machine import UART
from micropython import const
from midi import Midi
from midi_timbre import MIDI_TIMBRE_BANK_0
from midi_chorus_reverberation import MIDI_REVERBERATION_PLATE
from midi_percussion_note import (
    MIDI_PERCUSSION_TIMBRE_1,
    MIDI_PERCUSSION_TIMBRE_1_NOTE_C_2_KICK_DRUM_1,
    MIDI_PERCUSSION_TIMBRE_1_NOTE_D_2_SNARE_DRUM_1,
    MIDI_PERCUSSION_TIMBRE_1_NOTE_F_SHARP_2_CLOSED_HI_HAT,
    MIDI_PERCUSSION_TIMBRE_1_NOTE_A_SHARP_2_OPEN_HI_HAT,
    MIDI_PERCUSSION_TIMBRE_1_NOTE_G_SHARP_2_PEDAL_HI_HAT,
)

MIDI_PIN: int = const(17)

CHANNEL: int = const(9)
CHANNEL_VOLUME: int = const(100)

REVERBERATION_VOLUME: int = const(127)
REVERBERATION_DELAY_FEEDBACK: int = const(100)

TEMPO_RANDOM_RANGE: int = const(5)
TEMPO_RANDOM_OFFSET: int = const(2)

MIN_TEMPO: int = const(40)
MAX_TEMPO: int = const(250)

TICK_SIZE: int = const(15)


BASS_DRUM_TICK = [127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0]
SNARE_DRUM_TICK = [0, 0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
HI_HAT_OPEN_TICK = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0]
HI_HAT_CLOSE_TICK = [127, 40, 80, 40, 127, 40, 80, 40, 127, 40, 80, 40, 127, 0, 0]
HI_HAT_PEDAL_TICK = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127]

assert len(BASS_DRUM_TICK) == TICK_SIZE, "BASS_DRUM_TICK size must be 15"
assert len(SNARE_DRUM_TICK) == TICK_SIZE, "SNARE_DRUM_TICK size must be 15"
assert len(HI_HAT_OPEN_TICK) == TICK_SIZE, "HI_HAT_OPEN_TICK size must be 15"
assert len(HI_HAT_CLOSE_TICK) == TICK_SIZE, "HI_HAT_CLOSE_TICK size must be 15"
assert len(HI_HAT_PEDAL_TICK) == TICK_SIZE, "HI_HAT_PEDAL_TICK size must be 15"

tempo: int = 120
uart = UART(2, baudrate=31250, tx=MIDI_PIN)
midi = Midi(uart)


def play_drum_note(midi_note: int, note_velocity: int):
    if note_velocity > 0:
        midi.note_on(CHANNEL, midi_note, note_velocity)
        midi.note_off(CHANNEL, midi_note)


midi.midi_reset()
midi.set_channel_timbre(CHANNEL, MIDI_TIMBRE_BANK_0, MIDI_PERCUSSION_TIMBRE_1)
midi.set_reverberation(
    CHANNEL,
    MIDI_REVERBERATION_PLATE,
    REVERBERATION_VOLUME,
    REVERBERATION_DELAY_FEEDBACK,
)
midi.set_channel_volume(CHANNEL, CHANNEL_VOLUME)

while True:
    for tick_no in range(TICK_SIZE):
        tempo += urandom.getrandbits(3) % TEMPO_RANDOM_RANGE - TEMPO_RANDOM_OFFSET
        tempo = max(MIN_TEMPO, min(tempo, MAX_TEMPO))

        play_drum_note(
            MIDI_PERCUSSION_TIMBRE_1_NOTE_C_2_KICK_DRUM_1,
            BASS_DRUM_TICK[tick_no],
        )
        play_drum_note(
            MIDI_PERCUSSION_TIMBRE_1_NOTE_D_2_SNARE_DRUM_1,
            SNARE_DRUM_TICK[tick_no],
        )
        play_drum_note(
            MIDI_PERCUSSION_TIMBRE_1_NOTE_F_SHARP_2_CLOSED_HI_HAT,
            HI_HAT_CLOSE_TICK[tick_no],
        )
        play_drum_note(
            MIDI_PERCUSSION_TIMBRE_1_NOTE_A_SHARP_2_OPEN_HI_HAT,
            HI_HAT_OPEN_TICK[tick_no],
        )
        play_drum_note(
            MIDI_PERCUSSION_TIMBRE_1_NOTE_G_SHARP_2_PEDAL_HI_HAT,
            HI_HAT_PEDAL_TICK[tick_no],
        )

        time.sleep_ms(tempo)
