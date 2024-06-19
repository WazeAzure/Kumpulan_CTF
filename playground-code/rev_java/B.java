package com;

/* compiled from: Main.java */
/* loaded from: rev.jar:com/B.class */
class B {
    private String a;
    private String b;

    /* JADX INFO: Access modifiers changed from: package-private */
    public B(String str, String str2) {
        this.a = str;
        this.b = str2;
    }

    public String a(String str) {
        StringBuilder sb = new StringBuilder(str);
        while (sb.length() % 4 != 0) {
            sb.append('=');
        }
        return sb.toString();
    }

    public void b() {
        if (!this.a.equals("aHR0cHM6Ly95b3V0dS5iZS9UQlRqNHZkdHFiZw==") || this.b.length() > 28) {
            System.out.println("ipb.link\\link-flag");
        } else if (new A(a(this.b)).d().equals(this.a)) {
            System.out.printf("ipb.link\\%s\n", this.b);
        } else {
            System.out.println("ipb.link\\link-flag");
        }
    }
}
