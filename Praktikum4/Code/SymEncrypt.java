import javax.crypto.*;
import java.security.*;
import java.util.Arrays;
import java.util.Base64;
import javax.crypto.spec.*;

/* 
 * Implementation of Exercise 2 (symmetric encryption)
 */
public class SymEncrypt {
    
    private static SecretKey getAESKey() {
        String algorithm = "AES-256";
        int keySize = 256;
        KeyGenerator keygen = null;
        
        try {
            keygen = KeyGenerator.getInstance("AES");
        } catch (NoSuchAlgorithmException e) {
            System.err.println("[ERROR]: Couldn't generate AES Instance\n...terminating");
            System.exit(0);
        }

        keygen.init(keySize);
        return keygen.generateKey();
    }

    private static IvParameterSpec getIvSpec() {
        SecureRandom prng = new SecureRandom();
        byte[] iv = new byte[16];
        prng.nextBytes(iv);
        return new IvParameterSpec(iv);
    }

    private static Cipher initCipher(SecretKey key, int opmode, IvParameterSpec ivSpec) {
        try {
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(opmode, key, ivSpec);  // initialize cipher with given key
        return cipher;
        } catch (Exception e) {
            System.err.println("[ERROR]: Couldn't generate Cipher instance.\n"+e);
            System.exit(0);
        }
        return null;
    }
    
    /*
     * Uses cipher to encrypt the given plain text.
     */
    private static byte[] encrypt(Cipher cipher, String plainText) {
        try {
            return cipher.doFinal(plainText.getBytes());
        } catch (Exception e) {
            System.err.println("[ERROR]: while encrypting plain text.");
            System.exit(0);
        }
        return null;
    }

    private static String decrypt(Cipher cipher, byte cipherText[]) {
        try {
            byte pt[] = cipher.doFinal(cipherText);
            return new String(pt);
        } catch (Exception e) {
            System.err.println("[ERROR]: while decrypting cipher text.");
            System.exit(0);
        }
        return null;
    }

    private static void printCipherText(byte cipherText[]) {
        Base64.Encoder encoder = Base64.getEncoder();
        String msg = encoder.encodeToString(cipherText);
        System.out.println("Cipher Text: " + msg);
    }

    public static void main(String[] args) throws InvalidKeyException, InvalidAlgorithmParameterException {
        String pt = "Neo... Wake up!";

        SecretKey key = getAESKey();
        IvParameterSpec ivSpec = getIvSpec();
        Cipher cipher = initCipher(key, Cipher.ENCRYPT_MODE, ivSpec);
        byte cipherText[] = encrypt(cipher, pt);

        printCipherText(cipherText);

        cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
        String new_pt = decrypt(cipher, cipherText);
        
        System.out.println("Plain Text: " + new_pt); 
    }
}
