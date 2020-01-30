import javax.crypto.*;
import java.security.*;
import java.util.Arrays;
import java.util.Base64;
import javax.crypto.spec.*;

class SignatureTest {

    private static KeyPair genKeyPair() throws NoSuchAlgorithmException {
        int keysize = 2000;
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");

        return kpg.generateKeyPair();
    }

    private static String sign(String pt, PrivateKey pk) throws NoSuchAlgorithmException, SignatureException, InvalidKeyException {
        Signature rsa = Signature.getInstance("SHA256withRSA");
        rsa.initSign(pk);
        rsa.update(pt.getBytes());
        byte signature[] = rsa.sign();
        Base64.Encoder encoder = Base64.getEncoder();
        return encoder.encodeToString(signature);
    }

    public static void main(String[] args) throws NoSuchAlgorithmException, SignatureException, InvalidKeyException {
        String pt = "Follow the white rabbit";
        KeyPair kp = genKeyPair();
        
        String signature = sign(pt, kp.getPrivate());

        System.out.println("Signature: " + signature);
    }
}
