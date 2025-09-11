package planes.components;
/**
 * This file holds a class that can be used to make really simple (and bad) planes.
 * You are able to change the plane type, reg number (does nothing),
 * and a few other variables.
 * 
 * @author 0xDarkStar
 * @version 11/21/2024
 */

import planes.components.PlaneEnums.*;

public class Plane
{
    // Plane Attributes
    private String regNumber;
    private int maxSpeed;
    private int stallSpeed;
    private Type planeType;
    private Size planeSize;

    // Plane 3D Position
    private double xPos; // North / South
    private double yPos; // Up / Down
    private double zPos; // East / West

    // Plane Absolute State  (- / +)
    private double absPitch; // Down / Up
    private double absRoll; // Left / Right
    private double absYaw; // Left / Right
    private int throttle; // Back / Forward
    private boolean gearDown;

    // Plane Relative State (according to its own "up")
    private double relativePitch;
    private double relativeYaw;

    // Rotation Speed Limits
    private double pitchSpeed;
    private double rollSpeed;
    private double yawSpeed;

    // Constructor
    public Plane(String regNumber, Type planeType, Size planeSize)
    {
        // Plane Details
        this.regNumber = regNumber;
        this.planeType = planeType;
        this.planeSize = planeSize;
        setMaxSpeed();

        // Plane Starting Pos (Origin)
        xPos = 0.0;
        yPos = 0.0;
        zPos = 0.0;

        // Plane Starting State
        absPitch = 0.0;
        absRoll = 0.0;
        absYaw = 0.0;
        throttle = 0;
        relativePitch = 0.0;
        relativeYaw = 0.0;
    }

    // Set various variables according to plane type and size
    private void setMaxSpeed()
    {
        switch (planeType) {
            case PASSENGER:
                maxSpeed = 883;
                break;
            case CARGO:
                maxSpeed = 775;
                break;
            case MILITARY:
                maxSpeed = 1125;
                break;
            case CIVILIAN_JET:
                maxSpeed = 883;
                break;
            case CIVILIAN_PROP:
                maxSpeed = 360;
                break;
            case CIVILIAN_TURBO:
                maxSpeed = 563;
                break;
        }
        switch (planeSize) {
            case SMALL:
                maxSpeed -= 214;
                break;
            case LARGE:
                maxSpeed += 174;
                break;
        }
    }

    // Get info on the plane
    /**
     * Return the reg number of the plane
     * 
     * @return the reg number of the plane
     */
    public String getRegNumber()
    {
        return regNumber;
    }

    /**
     * Returns an array with all 3 axis of rotation and their current values.
     * The form is {Pitch, Roll, Yaw}
     * 
     * @return an array with values for each axis of rotation
     */
    public double[] getRotations()
    {
        double[] rotations = {absPitch, absRoll, absYaw};
        return rotations;
    }

    /**
     * Print all of the plane's data at once.
     */
    public void displayStatus()
    {
        System.out.println("\n\nPlane Status: ");
        System.out.println("Registration Number: " + regNumber);
        System.out.println("Plane Type: " + planeSize + " " + planeType);
        System.out.println("Current Speed: " + maxSpeed*(throttle/100.0) + " km/h\n");

        System.out.printf("Pitch: %.2f\u00B0\n", absPitch);
        System.out.printf("Roll: %.2f\u00B0\n", absRoll);
        System.out.printf("Yaw: %.2f\u00B0\n", absYaw);
        System.out.println("Throttle: " + throttle + "%\n");

        System.out.println("Plane Position: ");
        System.out.printf("X: %.2f\n", xPos);
        System.out.printf("Y: %.2f\n", yPos);
        System.out.printf("Z: %.2f\n", zPos);
    }

    // Control the plane
    /**
     * Adjust the relative pitch of the plane
     * 
     * @param degrees the number of degrees the plane pitches
     */
    public void adjustPitch(int degrees) {
        relativePitch += degrees;
        
        // Keep pitch within -360 to 360
        relativePitch = relativePitch % 360;
        
        // Adjust sign based on number of full rotations
        if (relativePitch % 180 > 90) {
            // Odd number of rotations flips the orientation
            relativePitch = relativePitch - 180;
        }
    }

    /**
     * Adjust the absolute roll of the plane
     * 
     * @param degrees the number of degrees the plane rolls
     */
    public void adjustRoll(int degrees)
    {
        absRoll += degrees;
        absRoll = absRoll%360; // If it makes a full rotation, just grab whats left
    }

    /**
     * Adjust the relative yaw of the plane
     * 
     * @param degrees the number of degrees the plane yaws
     */
    public void adjustYaw(int degrees)
    {
        relativeYaw += degrees;
        relativeYaw = relativeYaw%360; // If it makes a full rotation, just grab whats left
    }

    /**
     * Adjust the throttle
     * 
     * @param percentage set the throttle to this variable
     */
    public void setThrottle(int percentage)
    {
        throttle = percentage;
        // Make sure the throttle doesn't go over the limit
        if (throttle > 100){ // Don't allow it to go faster than its max speed
            throttle = 100;
        } else if (throttle < -100){ // Don't allow it to go faster than its max speed in reverse (I'm too lazy to slow down the reverse speed)
            throttle = -100;
        }
    }

    /**
     * The plane moves itself according to its pitch, yaw, roll, and throttle.
     * 
     */
    public void moveSelf()
    {
        relativeToAbsolute(); // Turn the relative rotations into absolute rotations (X,Y,Z instead of up, down, left, right)
        // Don't have a value that is -0.0000000000000000000000975849365943 (Really annoying)
        if (absPitch < 0.0001 && absPitch > -0.0001){
            absPitch = 0;
        }
        if (absRoll < 0.0001 && absRoll > -0.0001){
            absRoll = 0;
        }
        if (absYaw < 0.0001 && absYaw > -0.0001){
            absYaw = 0;
        }
        // Reset relative pitch and yaw
        relativePitch = 0; relativeYaw = 0;
        // Calculate the distance and direction the plane moves in
        moveForward();
    }

    // Calculations
    /**
     * Turn the relative movements of the plane to absolute movements
     */
    private void relativeToAbsolute()
    {
        // If the roll value is 90 or 270 (or anything bigger that is still on that line), swap the inputs
        if (absRoll%180 == 90)
        {
            absYaw += relativePitch;
            absPitch += relativeYaw;
        }
        // If it isn't, do what is normally done
        else {
        // Convert degrees to radians
        double pitchRad = Math.toRadians(relativePitch);
        double yawRad = Math.toRadians(relativeYaw);
        double rollRad = Math.toRadians(absRoll);

        // Calculate changes caused by pitch
        double yawChange = Math.asin(Math.sin(pitchRad) * Math.sin(rollRad));
        double pitchChange = pitchRad * Math.cos(rollRad);

        // Calculate changes cause by yaw
        pitchChange += Math.asin(Math.sin(yawRad) * Math.sin(rollRad));
        yawChange += yawRad * Math.cos(rollRad);

        // Convert back to degrees
        absYaw += Math.toDegrees(yawChange);
        absPitch += Math.toDegrees(pitchChange);
        }
    }

    /**
     * Using the absolute pitch, roll, yaw, and throttle, it determines how far in each axis it moves.
     */
    private void moveForward()
    {
        // Calculate actual speed based on throttle percentage
        double speed = (throttle / 100.0) * maxSpeed;
        
        // Convert angles to radians for trigonometric calculations
        double pitchRad = Math.toRadians(absPitch);
        double yawRad = Math.toRadians(absYaw);
        
        // Calculate movement components
        // X axis (North/South) - Affected by yaw and pitch
        xPos += speed * Math.cos(yawRad) * Math.cos(pitchRad);
        
        // Y axis (Up/Down) - Affected by pitch
        yPos += speed * Math.sin(pitchRad);
        
        // Z axis (East/West) - Affected by yaw and pitch
        zPos += speed * Math.sin(yawRad) * Math.cos(pitchRad);
    }
}