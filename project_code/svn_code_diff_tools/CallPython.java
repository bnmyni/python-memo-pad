import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;

/**
 * Copyright © 2008   卓望公司
 * package: com.scoco.pdshow
 * fileName: CallPython.java
 * version: 1.0.0.0
 * author: sunke
 * date: 2018/07/12 10:32
 */
public class CallPython {

    public static void main(String[] args) {
        try {
            Process process = Runtime.getRuntime().exec("python svn_diff.py https://10.1.3.80:8443/svn/UMP_PROJECT/tags/UMP2.0.4.0_SSYT_15 https://10.1.3.80:8443/svn/UMP_PROJECT/tags/UMP2.0.5.0_SSYT_15");
            InputStream is = process.getInputStream();
            DataInputStream dis = new DataInputStream(is);
            String str = dis.readLine();
            process.waitFor();
            while (str != null) {
                System.out.println(str);
                str = dis.readLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e1) {
            e1.printStackTrace();
        }
    }
}
