from desmume.emulator import DeSmuME

emu = DeSmuME()
emu.open('ROMs/Pokemon - Diamond Version (USA) (Rev 5).nds')

window = emu.create_sdl_window()
emu.volume_set(0)

while not window.has_quit():
    window.process_input()
    emu.cycle()
    window.draw()