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

    private static byte[] sign(String pt, PrivateKey pk) throws NoSuchAlgorithmException, SignatureException, InvalidKeyException {
        Signature rsa = Signature.getInstance("SHA256withRSA");
        rsa.initSign(pk); // initialize this object fo signing
        rsa.update(pt.getBytes()); // update the data to be signed
        byte signature[] = rsa.sign();  // sign data
        return signature;
    }

    private static boolean verify(String pt, byte[] signature, PublicKey pk) throws NoSuchAlgorithmException, SignatureException, InvalidKeyException {
        Signature sigInst = Signature.getInstance("SHA256withRSA");
        sigInst.initVerify(pk); // initialize this object for verification
        sigInst.update(pt.getBytes()); // updates the data to be verified
        return sigInst.verify(signature);
    }

    public static void main(String[] args) throws NoSuchAlgorithmException, SignatureException, InvalidKeyException {
        String pt = "Follow the white rabbit";
        KeyPair kp = genKeyPair();
        
        byte[] signature = sign(pt, kp.getPrivate());

        System.out.println("Text: " + pt);
        System.out.println("Signature: " + Base64.getEncoder().encodeToString(signature));
        System.out.println("Verifying document...");
        System.out.println("Verified: " + verify(pt, signature, kp.getPublic()));
        System.out.println("\n\nMutate text...");
        pt = pt + " clown";
        System.out.println("Text: " + pt);
        System.out.println("Verifying document...");
        System.out.println("Verified: " + verify(pt, signature, kp.getPublic()));
    }
}
