"""

author: Angelica Uzo
course: Chemical Engineering
school: University of Birmingham

"""

# This code will model the trajectory of a projectile with no drag starting from the ground, with an initial speed 
# of 10m s^-1 at 30 and 60 degrees from the horizontal at initial time, t0 in steps dt until final time, tf is reached
# using Euler and Velocity Verlet
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set_style("whitegrid")

def Euler(theta):
    # Pre-defined parameters
    # Initial position
    ry0 = 0 #m
    rx0 = 0 #m
    
    # Initial speed and angle of inclination to the horizontal
    v0 = 10 #m s^-1
    
    # Gravitational acceleration
    g = 9.81 #m s^-2
    
    # Initial time
    t0 = 0 #s
    
    # User-defined parameters
    # Time step                                      
    dt = 0.001 #s
    
    # Final time
    tf = 10 #s 
    
    # t_current represents the time at the current position of the projectile
    t_current = t0
    # r_current is an array containing the current vertical and horizontal displacements of the projectile respectively 
    r_current = np.array([ry0 , rx0]) 
    # v_current is an array containing the current vertical and horizontal velocities of the projectile respectively
    v_current = np.array([v0 * np.sin(np.radians(theta)) , v0 * np.cos(np.radians(theta))])
    # position and time represent empty lists into which the r_current and t_current 
    # values will be appended respectively
    position = []
    
    # Euler's Method
    # This loop calculates r_current at t_current and appends it to the list 'position' until t_current
    # is equal to tf after which, the loop is terminated. 
    while t_current <= tf:
        # r_current[0] represents the vertical displacement, r_current[1] represents the horizontal displacement
        # v_current[0] represents the vertical velocity, v_current[1] represents the horizontal velocity
        v_new = np.array([v_current[0] - g * dt , v_current[1] + 0 * dt])
        r_new = np.array([r_current[0] + v_current[0] * dt , r_current[1] + v_current[1] * dt])
        # 'position.append(r_current)' modifies the list 'position' by adding r_current to the end of the list 
        # rx_and_ry represents an array of the entries within 'position'
        position.append(r_current)
        rx_and_ry = np.array(position)
        # r_new and v_new become the next timestep's r_current and v_current values
        v_current = v_new
        r_current = r_new
        # 'time.append(t_current)' modifies the list 'time' by adding t_current to the end of the list 
        # t represents an array of the entries within 'time'
        # This defines t_current at the new timestep and the loop repeats
        t_current = t_current + dt
        # The 'if' condition breaks the loop when r_current[0] is negative, restricting the vertical 
        # displacement to values >= 0 
        if r_current[0] < 0:
            break
    return rx_and_ry
    
Euler_position_30 = Euler(30)
Euler_position_60 = Euler(60)
# Velocity Verlet
def verlet(theta):
    v0 = 10
    # Initial velocity in horizontal and vertical directions
    vx = v0 * np.cos(np.radians(theta))  
    vy = v0 * np.sin(np.radians(theta))
    # Initial position
    rx = 0
    ry = 0
    # Gravitational acceleration
    g = -9.81 ##acceleartion in y direction
    # Initial time
    t = 0 
    # Time step
    dt = 0.001 
    
    # RX and RY are arrays for collecting data
    RX = [rx]  
    RY = [ry]
    # Setting up the condition for a loop
    while(ry >=0):  
        # vx remains the same during the motion
        rx += vx*dt   
        ry += vy*dt/2  
        vy += g*dt  
        ry += vy*dt/2
        # defining the new time t
        t+=dt
       
        # Appending into RX and RY
        RX.append(rx)
        RY.append(ry)
    return RX, RY

X_verlet_30, Y_verlet_30 = verlet(30)
X_verlet_60, Y_verlet_60 = verlet(60)

# Plotting the graphs
# rx_and_ry[:,1] represents the Euler's horizontal displacement
# rx_and_ry[:,0] represents the Euler's vertical displacement
plt.scatter(Euler_position_30[:,1], Euler_position_30[:,0], label='Euler Projectile 30º')
plt.scatter(Euler_position_60[:,1], Euler_position_60[:,0], label='Euler Projectile 60º')
# A line graph is produced for the analytical data
plt.plot(X_verlet_30, Y_verlet_30, c='r', label='Velocity Verlet 30º')
plt.plot(X_verlet_60, Y_verlet_60, c='b', label='Velocity Verlet 60º')
plt.title("Trajectory of the Projectile")
plt.xlabel("Horizontal displacement ($m$)")
plt.ylabel("Vertical displacement ($m$)")
plt.legend(loc="upper right")

plt.show()

# Range represents the maximum horizontal distance the projectile travels
# Maximum height represents the maximum vertical distance the projectile travels
# Euler's range is detemined by finding the maximum value in rx_and_ry[:,1]
# Euler's maximum height is detemined by finding the maximum value in rx_and_ry[:,0]
print("At 30 degrees from the horizontal,")
range_verlet_30 = max(X_verlet_30)
max_height_verlet_30 = max(Y_verlet_30)
print ("Velocity Verlet Maximum Height of Projectile =", round(max_height_verlet_30, 3),"m")
print ("Velocity Verlet Range of Projectile  =", round(range_verlet_30, 3),"m")

range_30 = max(Euler_position_30[:,1])
max_height_30 = max(Euler_position_30[:,0])
print ("Euler's Maximum Height of Projectile at =", round(max_height_30, 3),"m")
print ("Euler's Range of Projectile =", round(range_30, 3),"m")

percent_diff_max_height_30 = (max_height_30 - max_height_verlet_30)/max_height_30 * 100
percent_diff_range_30 = (range_30 - range_verlet_30)/range_30 * 100
print ("Percentage difference for Maximum Height of Projectile =", abs(round(percent_diff_max_height_30, 3)),"%")
print ("Percentage difference for Range of Projectile =", abs(round(percent_diff_range_30, 3)),"%")
print("")
print("At 60 degrees from the horizontal,")
range_verlet_60 = max(X_verlet_60)
max_height_verlet_60 = max(Y_verlet_60)
print ("Velocity Verlet Maximum Height of Projectile =", round(max_height_verlet_60, 3),"m")
print ("Velocity Verlet Range of Projectile =", round(range_verlet_60, 3),"m")

range_60 = max(Euler_position_60[:,1])
max_height_60 = max(Euler_position_60[:,0])
print ("Euler's Maximum Height of Projectile =", round(max_height_60, 3),"m")
print ("Euler's Range of Projectile =", round(range_60, 3),"m")

percent_diff_max_height_60 = (max_height_60 - max_height_verlet_60)/max_height_60 * 100
percent_diff_range_60 = (range_60 - range_verlet_60)/range_60 * 100
print ("Percentage difference for Maximum Height of Projectile =", abs(round(percent_diff_max_height_60, 3)),"%")
print ("Percentage difference for Range of Projectile =", abs(round(percent_diff_range_60, 3)),"%")
