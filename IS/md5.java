import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5Example {
    public static void main(String[] args) {
        String text = "Hello, world!";
        
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            
            md.update(text.getBytes());
            
            byte[] digest = md.digest();
            
            StringBuilder sb = new StringBuilder();
            for (byte b : digest) {
                sb.append(String.format("%02x", b & 0xff));
            }
            
            System.out.println("MD5 Hash: " + sb.toString());
        } catch (NoSuchAlgorithmException e) {
            System.err.println("MD5 algorithm not found.");
            e.printStackTrace();
        }
    }
}
