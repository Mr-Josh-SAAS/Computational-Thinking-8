from random import randint
# Mature knight
guard = randint(1,6) + randint(1,6)
vig = randint(1,12) + 6
cla = randint(1,12) + 6
spi = randint(1,12) + 6

# squire
s_vig = randint(1,6) + randint(1,6) 
s_cla = randint(1,6) + randint(1,6) 
s_spi = randint(1,6) + randint(1,6) 

print(f"Knight: G={guard}, VIG={vig}, CLA={cla}, SPI={spi}")
print(f"Squire: G=1, VIG={s_vig}, CLA={s_cla}, SPI={s_spi}")

print("")

# aging them
n_vig = randint(1,6) + randint(1,12) 
n_cla = randint(1,6) + randint(1,12) 
n_spi = randint(1,6) + randint(1,12) 
print(f"New stats: VIG={n_vig}, CLA={n_cla}, SPI={n_spi}")

lost_vig = randint(1,12)
print(f"If alread old, lose {lost_vig} VIG")