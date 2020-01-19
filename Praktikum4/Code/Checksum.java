import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Checksum {

    /**
     *  Example of how to create and verify a checksum in Java.
     *
     */
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String exampleMessage1 = "Java is fun! (NOT)";
        String exampleMessage2 = "Java is fun!";
        byte[] checksum = createChecksum(exampleMessage1);

        boolean eq = verifyChecksum(checksum, exampleMessage1);
        System.out.println("Checksums are equal: " + eq);

        eq = verifyChecksum(checksum, exampleMessage2);
        System.out.println("Checksums are equal: " + eq);
    }

    /**
     * Create a hash checksum for a string
     *
     * @param message The message that is hashed
     * @return A byte Array with the checksum
     * @throws NoSuchAlgorithmException
     */
    public static byte[] createChecksum(String message) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        return md.digest(message.getBytes());
    }

    /**
     * Checks whether a checksum is the hash of a message
     * @param checksum A previously created checksum for any message
     * @param message The message which is checked against
     * @return true when the checksum and the hash of the message are equal
     * @throws NoSuchAlgorithmException when SHA-256 is not available
     */
    public static boolean verifyChecksum(byte[] checksum, String message) throws NoSuchAlgorithmException {
        byte[] actual = createChecksum(message);
        return MessageDigest.isEqual(actual, checksum);
    }
}
