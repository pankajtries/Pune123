public class MD5Example {
    public static void main(String[] args) {
        String text = "Hello, World!";
        String md5Hash = getMD5Hash(text);
        System.out.println("MD5 hash of \"" + text + "\" is: " + md5Hash);
    }

    public static String getMD5Hash(String input) {
        int[] k = new int[64];
        for (int i = 0; i < 64; i++) {
            k[i] = (int) (Math.pow(2, 32) * Math.abs(Math.sin(i + 1)));
        }

        int[] s = {7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
                4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21};

        byte[] data = input.getBytes();
        int a = 0x67452301, b = 0xEFCDAB89, c = 0x98BADCFE, d = 0x10325476;

        for (int i = 0; i < data.length; i += 64) {
            int[] m = new int[16];
            for (int j = 0; j < 16; j++) {
                m[j] = (data[i + j * 4] & 0xFF)
                        | (data[i + j * 4 + 1] & 0xFF) << 8
                        | (data[i + j * 4 + 2] & 0xFF) << 16
                        | (data[i + j * 4 + 3] & 0xFF) << 24;
            }

            int aa = a, bb = b, cc = c, dd = d;

            a = ff(a, b, c, d, m[0], s[0], k[0]);
            d = ff(d, a, b, c, m[1], s[1], k[1]);
            c = ff(c, d, a, b, m[2], s[2], k[2]);
            b = ff(b, c, d, a, m[3], s[3], k[3]);
            a = ff(a, b, c, d, m[4], s[4], k[4]);
            d = ff(d, a, b, c, m[5], s[5], k[5]);
            c = ff(c, d, a, b, m[6], s[6], k[6]);
            b = ff(b, c, d, a, m[7], s[7], k[7]);
            a = ff(a, b, c, d, m[8], s[8], k[8]);
            d = ff(d, a, b, c, m[9], s[9], k[9]);
            c = ff(c, d, a, b, m[10], s[10], k[10]);
            b = ff(b, c, d, a, m[11], s[11], k[11]);
            a = ff(a, b, c, d, m[12], s[12], k[12]);
            d = ff(d, a, b, c, m[13], s[13], k[13]);
            c = ff(c, d, a, b, m[14], s[14], k[14]);
            b = ff(b, c, d, a, m[15], s[15], k[15]);

            a = gg(a, b, c, d, m[1], s[16], k[16]);
            d = gg(d, a, b, c, m[6], s[17], k[17]);
            c = gg(c, d, a, b, m[11], s[18], k[18]);
            b = gg(b, c, d, a, m[0], s[19], k[19]);
            a = gg(a, b, c, d, m[5], s[20], k[20]);
            d = gg(d, a, b, c, m[10], s[21], k[21]);
            c = gg(c, d, a, b, m[15], s[22], k[22]);
            b = gg(b, c, d, a, m[4], s[23], k[23]);
            a = gg(a, b, c, d, m[9], s[24], k[24]);
            d = gg(d, a, b, c, m[14], s[25], k[25]);
            c = gg(c, d, a, b, m[3], s[26], k[26]);
            b = gg(b, c, d, a, m[8], s[27], k[27]);
            a = gg(a, b, c, d, m[13], s[28], k[28]);
            d = gg(d, a, b, c, m[2], s[29], k[29]);
            c = gg(c, d, a, b, m[7], s[30], k[30]);
            b = gg(b, c, d, a, m[12], s[31], k[31]);

            a = hh(a, b, c, d, m[5], s[32], k[32]);
            d = hh(d, a, b, c, m[8], s[33], k[33]);
            c = hh(c, d, a, b, m[11], s[34], k[34]);
            b = hh(b, c, d, a, m[14], s[35], k[35]);
            a = hh(a, b, c, d, m[1], s[36], k[36]);
            d = hh(d, a, b, c, m[4], s[37], k[37]);
            c = hh(c, d, a, b, m[7], s[38], k[38]);
            b = hh(b, c, d, a, m[10], s[39], k[39]);
            a = hh(a, b, c, d, m[13], s[40], k[40]);
            d = hh(d, a, b, c, m[0], s[41], k[41]);
            c = hh(c, d, a, b, m[3], s[42], k[42]);
            b = hh(b, c, d, a, m[6], s[43], k[43]);
            a = hh(a, b, c, d, m[9], s[44], k[44]);
            d = hh(d, a, b, c, m[12], s[45], k[45]);
            c = hh(c, d, a, b, m[15], s[46], k[46]);
            b = hh(b, c, d, a, m[2], s[47], k[47]);

            a = ii(a, b, c, d, m[0], s[48], k[48]);
            d = ii(d, a, b, c, m[7], s[49], k[49]);
            c = ii(c, d, a, b, m[14], s[50], k[50]);
            b = ii(b, c, d, a, m[5], s[51], k[51]);
            a = ii(a, b, c, d, m[12], s[52], k[52]);
            d = ii(d, a, b, c, m[3], s[53], k[53]);
            c = ii(c, d, a, b, m[10], s[54], k[54]);
            b = ii(b, c, d, a, m[1], s[55], k[55]);
            a = ii(a, b, c, d, m[8], s[56], k[56]);
            d = ii(d, a, b, c, m[15], s[57], k[57]);
            c = ii(c, d, a, b, m[6], s[58], k[58]);
            b = ii(b, c, d, a, m[13], s[59], k[59]);
            a = ii(a, b, c, d, m[4], s[60], k[60]);
            d = ii(d, a, b, c, m[11], s[61], k[61]);
            c = ii(c, d, a, b, m[2], s[62], k[62]);
            b = ii(b, c, d, a, m[9], s[63], k[63]);

            a = (a + aa) & 0xFFFFFFFF;
            b = (b + bb) & 0xFFFFFFFF;
            c = (c + cc) & 0xFFFFFFFF;
            d = (d + dd) & 0xFFFFFFFF;
        }

        return String.format("%08X%08X%08X%08X", a, b, c, d);
    }

    private static int ff(int a, int b, int c, int d, int x, int s, int k) {
        a += (b & c | (~b & d)) + x + k;
        return (a << s | a >>> (32 - s)) + b;
    }

    private static int gg(int a, int b, int c, int d, int x, int s, int k) {
        a += (b & d | c & ~d) + x + k;
        return (a << s | a >>> (32 - s)) + b;
    }

    private static int hh(int a, int b, int c, int d, int x, int s, int k) {
        a += (b ^ c ^ d) + x + k;
        return (a << s | a >>> (32 - s)) + b;
    }

    private static int ii(int a, int b, int c, int d, int x, int s, int k) {
        a += (c ^ (b | ~d)) + x + k;
        return (a << s | a >>> (32 - s)) + b;
    }
}