
import java.util.ArrayList;
import java.util.Base64;
import java.util.Collections;

import java.util.Scanner;


/* JADX INFO: Access modifiers changed from: package-private */
/* compiled from: Main.java */
/* loaded from: rev.jar:com/A.class */
class A {
    int[] a = {0, 23, 0, 29, 4, 29, 27, 1, 0, 9, 22, 0, 4, 28, 7, 6, 19, 24, 12, 24, 20, 6, 10, 28, 14, 16, 23, 21, 14, 1, 23, 6, 4, 19, 23, 0, 0, 8, 7, 25, 5, 8, 12, 11, 9, 9, 2, 16, 24, 28, 17, 2, 20, 10, 24, 5, 4, 23, 23, 17, 9, 14, 14, 15, 4, 11, 23, 1, 25, 12, 1, 4, 19, 22, 3, 25, 25, 22, 16, 28, 4, 24, 6, 10, 19, 21, 14, 7, 19, 19, 22, 2, 24, 23, 19, 15, 4, 3, 28, 20, 19, 3, 26, 27, 19, 2, 4, 18, 15, 3, 10, 22};
    ArrayList<Integer> b = new ArrayList<>();

    /* JADX INFO: Access modifiers changed from: package-private */
    public A(String str) {
        a(str);
    }

    /* JADX WARN: Multi-variable type inference failed */
    /* JADX WARN: Type inference failed for: r0v14, types: [int] */
    public void a(String str) {
        for (int length = str.length() - 1; length >= 0; length--) {
            char charAt = str.charAt(length);
            for (int i = 0; i < 7; i++) {
                this.b.add(Integer.valueOf(charAt % 2));
                charAt /= 2;
            }
        }
        Collections.reverse(this.b);
    }

    public int b(int i) {
        int i2 = 1;
        int i3 = 0;
        for (int i4 = i + 27; i4 >= i; i4--) {
            i3 += this.b.get(i4).intValue() * i2;
            i2 *= 2;
        }
        return i3;
    }

    public void c() {
        for (int i = 0; i < this.b.size(); i += 28) {
            int b = b(i);
            int i2 = (((b >> 4) & 15) << 20) | (((b >> 16) & 15) << 8) | (((b >> 20) & 15) << 16) | ((b >> 12) & 15) | (((b >> 8) & 15) << 24) | ((b & 15) << 12) | (((b >> 24) & 15) << 4);
            for (int i3 = i + 27; i3 >= i; i3--) {
                this.b.set(i3, Integer.valueOf(i2 % 2));
                i2 /= 2;
            }
        }
    }

    public String d() {
        c();
        for (int i = 0; i < 112 && i < this.b.size(); i++) {
            this.b.set(i, Integer.valueOf((this.b.get(i).intValue() + this.a[i]) % 5));
        }
        StringBuilder sb = new StringBuilder("");
        for (int i2 = 0; i2 < this.b.size() / 4; i2++) {
            int i3 = 0;
            int i4 = 1;
            for (int i5 = ((i2 + 1) * 4) - 1; i5 >= i2 * 4; i5--) {
                i3 += i4 * this.b.get(i5).intValue();
                i4 *= 5;
            }
            if (i3 > 256) {
                sb.append('=');
            } else {
                sb.append((char) i3);
            }
        }
        return new String(Base64.getEncoder().encode(sb.toString().getBytes()));
    }
}

/* compiled from: Main.java */
/* loaded from: rev.jar:com/B.class */
class B {
    private String a;
    private String b;

    /* JADX INFO: Access modifiers changed from: package-private */
    public B(String str, String str2) {
        this.a = str;
        this.b = str2;
		System.out.println(this.a + " " + this.b);
    }

    public String a(String str) {
        StringBuilder sb = new StringBuilder(str);
        while (sb.length() % 4 != 0) {
            sb.append('=');
        }
        return sb.toString();
    }

    public void b() {
		System.out.println(new A(a(this.b)).d());
		System.out.println(this.a);
        if (!this.a.equals("aHR0cHM6Ly95b3V0dS5iZS9UQlRqNHZkdHFiZw==") || this.b.length() > 28) {
            System.out.println("ipb.link\\link-flag");
        } else if (new A(a(this.b)).d().equals(this.a)) {
            System.out.printf("ipb.link\\%s\n", this.b);
        } else {
            System.out.println("ipb.link\\link-flag");
        }
    }
}

/* loaded from: rev.jar:com/Main.class */
public class Main {
    public static void main(String[] args) {
        String str = System.getenv("checker");
        if (str == null) {
            str = "";
        }
        System.out.print("masukkan input: ");
        Scanner scanner = new Scanner(System.in);
        new B(new String(Base64.getEncoder().encode(str.getBytes())), scanner.next().replace("=", "")).b();
        scanner.close();
    }
}
