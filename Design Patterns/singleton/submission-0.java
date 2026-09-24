static class Singleton {

    private static Singleton uniqueSingleton = null;

    private String value = null;

    private Singleton() {

    }

    public static Singleton getInstance() {
        if (uniqueSingleton == null) {
            uniqueSingleton = new Singleton();
        }
        return uniqueSingleton;
    }

    public String getValue() {
        return this.value;
    }

    public void setValue(String value) {
        this.value = value;
    }
}
