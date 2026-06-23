from micropython import const

# Reverberation effect type constants

# Room reverberation type 1
MIDI_REVERBERATION_ROOM_1: int = const(0)

# Room reverberation type 2
MIDI_REVERBERATION_ROOM_2: int = const(1)

# Room reverberation type 3
MIDI_REVERBERATION_ROOM_3: int = const(2)

# Hall reverberation type 1
MIDI_REVERBERATION_HALL_1: int = const(3)

# Hall reverberation type 2
MIDI_REVERBERATION_HALL_2: int = const(4)

# Plate reverberation effect
MIDI_REVERBERATION_PLATE: int = const(5)

# Delay reverberation effect
MIDI_REVERBERATION_DELAY: int = const(6)

# Panning delay reverberation effect
MIDI_REVERBERATION_PAN_DELAY: int = const(7)

# Chorus effect type constants

# Chorus effect type 1
MIDI_CHORUS_1: int = const(0)

# Chorus effect type 2
MIDI_CHORUS_2: int = const(1)

# Chorus effect type 3
MIDI_CHORUS_3: int = const(2)

# Chorus effect type 4
MIDI_CHORUS_4: int = const(3)

# Feedback chorus effect
MIDI_CHORUS_FEEDBACK: int = const(4)

# Flanger-style chorus effect
MIDI_CHORUS_FLANGER: int = const(5)

# Short delay chorus effect
MIDI_CHORUS_SHORT_DELAY: int = const(6)

# Feedback delay chorus effect
MIDI_CHORUS_FEEDBACK_DELAY: int = const(7)
