package planes.components;

public class PlaneEnums {
    public enum Type {
        PASSENGER("Passenger", 883, 0.15),
        CARGO("Cargo", 775, 0.12),
        MILITARY("Military", 1125, 0.20),
        CIVILIAN_JET("Civilian Jet", 883, 0.15),
        CIVILIAN_PROP("Civilian Prop", 360, 0.25),
        CIVILIAN_TURBO("Civilian Turbo", 563, 0.18);
    
        private final String displayName;
        private final int baseSpeed; // Speed for MEDIUM size
        private final double turnRate;
    
        Type(String displayName, int baseSpeed, double turnRate) {
            this.displayName = displayName;
            this.baseSpeed = baseSpeed;
            this.turnRate = turnRate;
        }
    
        public String getDisplayName() { return displayName; }
        public int getBaseSpeed() { return baseSpeed; }
        public double getTurnRate() { return turnRate; }
    
        // Returns speed multiplier based on size
        public double getSpeedMultiplier(Size size) {
            switch (this) {
                case PASSENGER:
                    switch (size) {
                        case SMALL: return 0.90;
                        case MEDIUM: return 1.0;
                        case LARGE: return 1.15;
                    }
                case CARGO:
                    switch (size) {
                        case SMALL: return 0.70;
                        case MEDIUM: return 1.0;
                        case LARGE: return 1.18;
                    }
                case MILITARY:
                    switch (size) {
                        case SMALL: return 0.75;
                        case MEDIUM: return 1.0;
                        case LARGE: return 1.25;
                    }
                case CIVILIAN_JET:
                    switch (size) {
                        case SMALL: return 0.65;
                        case MEDIUM: return 1.0;
                        case LARGE: return 1.15;
                    }
                case CIVILIAN_PROP:
                    switch (size) {
                        case SMALL: return 0.50;  // Ultralight aircraft
                        case MEDIUM: return 1.0;
                        case LARGE: return 1.20;
                    }
                case CIVILIAN_TURBO:
                    switch (size) {
                        case SMALL: return 0.70;
                        case MEDIUM: return 1.0;
                        case LARGE: return 1.25;
                    }
            }
            return 1.0; // Default fallback, though this should never be reached
        }
    }
    
    public enum Size {
        SMALL("Small"),
        MEDIUM("Medium"),
        LARGE("Large");
    
        private final String displayName;
    
        Size(String displayName) {
            this.displayName = displayName;
        }
    
        public String getDisplayName() { return displayName; }
    }
    public enum State {
        LANDED,
        FLYING,
        STALLED,
        CRASHED
    }
}
