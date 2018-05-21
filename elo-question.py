# Using this article as a basis: https://metinmediamath.wordpress.com/2013/11/27/how-to-calculate-the-elo-rating-including-example/

print("Scenario: If you are a ELO 2000 player, why can't you play against an ELO 400 player enough times that you get infnite ELO?\n")

r1 = 2000
r2 = 400

R1 = 10**(r1/r2) # 10^(2400/400) = 100,000
R2 = 10**(r2/r1) # 10^(800/400) = 10

E1 = R1/(R1+R2) # 100,000/(100,000+10) = 0.99990000999
E2 = R2/(R1+R2) # 100,000/(100,000+10) = 0.00009999

# In this case, player 1 with the high ELO wins
S1 = 1
S2 = 0

# K = 32 for players below 2000 
K = 32

# New rating values
r1 = r1 + K*(S1-E1) # 2000.00319968
r2 = r2 + K*(S2-E2) # 399.99680032

print("Player 1 now has an ELO of " + str(r1))
print("Player 2 now has an ELO of " + str(r2))

print("\nAnswer: If you are a 2000 ELO player, you would have to play 10000 games against a 400 ELO player to gain a single point.")
