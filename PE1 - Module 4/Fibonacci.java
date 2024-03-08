public final class Fibonacci {

    public static void main(String[] args) {
        var number = Integer.parseInt(args[0]);
        System.out.println(number + " -> " + fibonacci(number));
    }

    private static final int fibonacci(int n) {
    
        if (n < 0) {
            return 0;
        }

        if (n < 3) {
            return 1;
        } 
       
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
