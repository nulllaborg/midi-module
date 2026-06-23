import time
from micropython import const
from machine import UART
from midi import Midi
from midi_chorus_reverberation import MIDI_REVERBERATION_ROOM_2
from midi_note import (
    MIDI_NOTE_G_4,
    MIDI_NOTE_A_4,
    MIDI_NOTE_C_5,
    MIDI_NOTE_B_4,
    MIDI_NOTE_D_5,
    MIDI_NOTE_E_5,
    MIDI_NOTE_G_5,
    MIDI_NOTE_F_5,
)
from midi_timbre import (
    MIDI_TIMBRE_BANK_0,
    MIDI_TIMBRE_BANK_0_ACOUSTIC_GUITAR_STEEL_STRING,
)

MIDI_PIN: int = const(17)

CHANNEL: int = const(0)
CHANNEL_VOLUME: int = const(110)

REVERBERATION_VOLUME: int = const(80)
REVERBERATION_DELAY_FEEDBACK: int = const(0)

QUARTER_NOTE_DURATION: int = const(300)
EIGHTH_NOTE_DURATION: int = 150
DOTTED_QUARTER_NOTE_DURATION: int = const(450)

uart = UART(2, baudrate=31250, tx=MIDI_PIN)
midi = Midi(uart)


def play_note(midi_note: int, duration: int, note_velocity: int = 90):
    midi.note_on(CHANNEL, midi_note, note_velocity)
    time.sleep_ms(duration)
    midi.note_off(CHANNEL, midi_note)
    time.sleep_ms(30)


midi.set_channel_timbre(
    CHANNEL,
    MIDI_TIMBRE_BANK_0,
    MIDI_TIMBRE_BANK_0_ACOUSTIC_GUITAR_STEEL_STRING,
)
midi.set_channel_volume(CHANNEL, CHANNEL_VOLUME)
midi.set_reverberation(
    CHANNEL,
    MIDI_REVERBERATION_ROOM_2,
    REVERBERATION_VOLUME,
    REVERBERATION_DELAY_FEEDBACK,
)

while True:
    play_note(MIDI_NOTE_G_4, EIGHTH_NOTE_DURATION)
    play_note(MIDI_NOTE_G_4, EIGHTH_NOTE_DURATION)
    play_note(MIDI_NOTE_A_4, QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_G_4, QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_C_5, DOTTED_QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_B_4, DOTTED_QUARTER_NOTE_DURATION)
    time.sleep_ms(QUARTER_NOTE_DURATION)

    play_note(MIDI_NOTE_G_4, EIGHTH_NOTE_DURATION)
    play_note(MIDI_NOTE_G_4, EIGHTH_NOTE_DURATION)
    play_note(MIDI_NOTE_A_4, QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_G_4, QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_D_5, DOTTED_QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_C_5, DOTTED_QUARTER_NOTE_DURATION)
    time.sleep_ms(QUARTER_NOTE_DURATION)

    play_note(MIDI_NOTE_G_4, EIGHTH_NOTE_DURATION)
    play_note(MIDI_NOTE_G_4, EIGHTH_NOTE_DURATION)
    play_note(MIDI_NOTE_G_5, QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_E_5, QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_C_5, QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_B_4, QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_A_4, DOTTED_QUARTER_NOTE_DURATION)
    time.sleep_ms(QUARTER_NOTE_DURATION)

    play_note(MIDI_NOTE_F_5, EIGHTH_NOTE_DURATION)
    play_note(MIDI_NOTE_F_5, EIGHTH_NOTE_DURATION)
    play_note(MIDI_NOTE_E_5, QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_C_5, QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_D_5, DOTTED_QUARTER_NOTE_DURATION)
    play_note(MIDI_NOTE_C_5, DOTTED_QUARTER_NOTE_DURATION)

    time.sleep_ms(5000)
