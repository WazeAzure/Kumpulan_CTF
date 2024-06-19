package com;

import java.util.Base64;
import java.util.Scanner;

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
