.include "header.inc"
.include "init.asm"

.BANK 0 SLOT 0
.ORG 0
.SECTION "MainCode"

Start:
  InitSNES            ; Init Snes :)

  sei
  clc
  xce
  rep #$10
  sep #$20

  lda #$80
  sta $4200

  stz $2121           ; Edit color 0 - snes' screen color
                      ; you can write it in binary or hex
  lda #%00011111      ; binary is more visual, but if you
  sta $2122           ; wanna be cool, use hex ;)
  stz $2122           ; second byte is 0, so we write a 0

  lda #$0F            ; = 00001111
  sta $2100           ; Turn on screen, full brightness
  lda #$00
    
Loop:
    jmp Loop

VBlank:
  stz $2121
  sta $2122
  sta $2122
  ina

.ENDS