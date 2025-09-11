package planes;

import planes.components.*; // Imports classes
import planes.components.PlaneEnums.*; // Imports enums

public class tester {
    public static void main(String[] args)
    {
        Plane testingPlane = new Plane("Reg Number", Type.PASSENGER, Size.SMALL);

        // Controls
        testingPlane.adjustPitch(0);
        testingPlane.adjustRoll(0);
        testingPlane.adjustYaw(0);
        testingPlane.setThrottle(0);

        // Get Info
        testingPlane.displayStatus();
        String regNum = testingPlane.getRegNumber();
        double[] rotations = testingPlane.getRotations();
    }
}
