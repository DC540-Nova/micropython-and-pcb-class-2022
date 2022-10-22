![image](https://github.com/DC540-Nova/micropython-and-pcb-class-2022/blob/main/micropython-and-pcb-class-2022.png?raw=true)

# MicroPython & PCB Class 2022
MicroPython & PCB Class 2022 Chapter 3 - Basic PCB Design.

<br>

# STEP 1: Create Project
```bash
file
new project
0x01-class
SAVE
```

double-click 0x01-class-kicad_sch
visit https://github.com/ncarandini/KiCad-RP-Pico
	code
		download ZIP
			(unzip file)
create, delete and edit footprints
	file
		add library
			global
				KiCad-RP-Pico-main
					RP-Pico Libraries
						MCU_RapsberryPi_and_Boards.kicad_sym
							select folder
place
	add symbol [a]
		(search) Pico
			MCU_RapsberryPi_and_Boards
				Pico
					OK
	add symbol [a]
		(search) WS2812B
			LED
				WS2812B
					OK
(hover over WS2812B, click and CTRL-C and CTRL-V)
(repeat 5x and place)
add a power port [p]
	(search) +3V3
		power
			+3V3
				OK
add a net label [l]
	3V3
		OK
(attach to wire hole on +3V3)
(click 3V3)
(click [m])
(attach to 3V3 on Pico)
(delete +3V3 and optional wire)
(hover over 3V3 on Pico, click and CTRL-C and CTRL-V)
(attach to wire hole on 1st WS2812B's VDD and repeat 5x for other WS2812B's)
add a net label [l]
	GND
		OK
(attach to GND Pin 38 on Pico)
(hover over GND on Pico, click and CTRL-C and CTRL-V)
(attach to other GND pins on Pico, [r] when necessary)
(hover over any GND on Pico, click and CTRL-C and CTRL-V)
(attach to wire hole on 1st WS2812B's VSS and repeat 5x for other WS2812B's)
add a net label [l]
	NP
		OK
(attach to GPIO18 on Pico)
(hover over NP and CTRL-C and CTRL-V 1x)
(hover over NP and CTRL-C and CTRL-V 1x)
(type [r] 2x and attach to DIN hole on 1st WS2812B)
add a wire [w]
	(attach to DOUT on 1st WS2812B and connect to DIN on 2nd WS2812B)
	(repeat process to remainder of WS2812B's)
open PCB in board editor
update PCB with changes made to schematic [F8]
	annotate
		update PCB
			close
create, delete and edit footprints
	file
		add library
			global
				KiCad-RP-Pico-main
					RP-Pico Libraries
						MCU_RapsberryPi_and_Boards.pretty
							select folder
								(search) RPi_Pico_SMD_TH
									(double-click)
										(save)
											(X)
open schematic in eeschema
(right-click inside empty area in Pico and click properties)
	(click footprint RPi_Pico-RPi_Pico_SMD_TH and click bookshelf icon and ok)
		(search) MCU_RaspberryPi_and_Boards
			(double-click) RPi_Pico_SMD_TH
				OK
open PCB in board editor
update PCB with changes made to schematic [F8]
	update PCB
		close
(arrange WS2812B's appropriately where GP18 connects to 1st WS2812B's NP, etc)
([r] when necessary)
(*NOTE: click in black area in center of WS2812B to move whole unit rather than pieces*)
edit board setup including layers, design rules and various defaults
	design rules
		net classes
			+
				PWR
					track width
						0.35 mm
							net
								/3V3
									net class
										PWR
								/GND
									net class
										PWR
											OK
route tracks [x]
	(click GP18 on Pico and conect to NP on first WS2812B)
	(connect 2nd to 3rd, etc)
	(click 3V3 on Pico and connect to 3V3 on first WS2812B)
	(connect 2nd to 3rd, etc)
edge cuts
	draw a rectangle
		(draw box around circuit)
F.Cu
	add a filled zone [CTRL-SHIFT-Z]
		(click) /GND
			ok
				(draw ouside board trace, click upper left and drag and click as appropriate)
				(double-click to finish)
fill all zones [b]
show the design rules checker window
	run DRC
		close
```

<br>

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
