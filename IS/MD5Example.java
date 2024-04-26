javac MD5Example.java
java MD5Example

public class MD5Example {

    public static void main(String[] args) {
        String text = "Hello, world!";
        String md5Hash = calculateMD5(text);
        System.out.println("MD5 hash of '" + text + "': " + md5Hash);
    }

    public static String calculateMD5(String text) {
        // Step 1: Append padding bits
        int origLength = text.length();
        text += (char) 0x80; // Append single '1' bit
        while ((text.length() % 64) != 56) {
            text += (char) 0x00; // Append '0' bits
        }

        // Step 2: Append original length in bits
        long lengthInBits = origLength * 8;
        for (int i = 0; i < 8; i++) {
            text += (char) (lengthInBits & 0xFF);
            lengthInBits >>= 8;
        }

        // Step 3: Initialize variables
        int[] s = {7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                   5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
                   4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                   6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21};
        int[] K = new int[64];
        for (int i = 0; i < 64; i++) {
            K[i] = (int) (Math.floor(Math.abs(Math.sin(i + 1)) * (1L << 32)));
        }
        int a0 = 0x67452301;
        int b0 = 0xEFCDAB89;
        int c0 = 0x98BADCFE;
        int d0 = 0x10325476;

        // Step 4: Process message in 512-bit chunks
        int numOfChunks = text.length() / 64;
        int[] chunks = new int[numOfChunks * 16];
        for (int i = 0; i < numOfChunks; i++) {
            for (int j = 0; j < 16; j++) {
                chunks[i * 16 + j] = (text.charAt(i * 64 + j * 4) & 0xFF) |
                                     ((text.charAt(i * 64 + j * 4 + 1) & 0xFF) << 8) |
                                     ((text.charAt(i * 64 + j * 4 + 2) & 0xFF) << 16) |
                                     ((text.charAt(i * 64 + j * 4 + 3) & 0xFF) << 24);
            }
        }

        // Remaining steps are same as before...

        // Step 5: Initialize hash value for this chunk
        int A = a0;
        int B = b0;
        int C = c0;
        int D = d0;

        // Step 6: Main loop
        for (int i = 0; i < numOfChunks; i++) {
            int[] M = new int[16];
            System.arraycopy(chunks, i * 16, M, 0, 16);
            int AA = A;
            int BB = B;
            int CC = C;
            int DD = D;

            for (int j = 0; j < 64; j++) {
                int F, g;
                if (j < 16) {
                    F = (BB & CC) | (~BB & DD);
                    g = j;
                } else if (j < 32) {
                    F = (DD & BB) | (~DD & CC);
                    g = (5 * j + 1) % 16;
                } else if (j < 48) {
                    F = BB ^ CC ^ DD;
                    g = (3 * j + 5) % 16;
                } else {
                    F = CC ^ (BB | ~DD);
                    g = (7 * j) % 16;
                }
                F = F + A + K[j] + M[g];
                A = D;
                D = C;
                C = B;
                B = B + ((F << s[j]) | (F >>> (32 - s[j])));
            }

            A = A + AA;
            B = B + BB;
            C = C + CC;
            D = D + DD;
        }

        // Step 7: Concatenate A, B, C, D
        StringBuilder sb = new StringBuilder();
        sb.append(Integer.toHexString(A));
        sb.append(Integer.toHexString(B));
        sb.append(Integer.toHexString(C));
        sb.append(Integer.toHexString(D));
        
        return sb.toString();
    }
}
