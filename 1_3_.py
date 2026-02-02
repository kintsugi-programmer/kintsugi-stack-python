sword_damage = 10
start_health = 100
# end_health = start_health + sword_damage # bug
end_health = start_health - sword_damage # fix

# Don't touch below this line
print(f"Sam's health is: {start_health}")
print(f"Sam takes {sword_damage} damage...")
print(f"Sam's health is: {end_health}")
# Sam's health is: 100
# Sam takes 10 damage...
# Sam's health is: 90