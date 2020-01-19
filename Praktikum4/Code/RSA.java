import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import java.security.*;
import java.util.Arrays;
import java.util.Base64;

public class RSA {

    public static void main(String[] args) throws InvalidKeyException, NoSuchPaddingException, NoSuchAlgorithmException, BadPaddingException, IllegalBlockSizeException {
        // INIT
        int keysize=2000;
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(keysize);
        KeyPair rsaKeyPair = keyPairGen.generateKeyPair();
        String plainText = "Kryptographie macht immer noch Spass!!!";
        System.out.println("Original message: " + plainText);
        PublicKey publicKey = rsaKeyPair.getPublic();
        Cipher rsa = Cipher.getInstance("RSA");
        // ENCRYPT
        rsa.init(Cipher.ENCRYPT_MODE, publicKey);
        byte[] cipherText = rsa.doFinal(plainText.getBytes());
        Base64.Encoder encoder = Base64.getEncoder();
        String message = encoder.encodeToString(cipherText);
        System.out.println("encrypted message: " + message);

        // DECRYPT
        rsa.init(Cipher.DECRYPT_MODE, rsaKeyPair.getPrivate());
        byte[] plainTextAgain = rsa.doFinal(cipherText);
        System.out.println("decrypted message : " + new String(plainTextAgain));
    }
}
