import java.sql.*;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class MahasiswaApp extends JFrame {
    // Komponen GUI
    private JTable table;
    private DefaultTableModel model;
    private JTextField txtNama, txtNIM, txtJurusan, txtAlamat;
    private JButton btnTambah, btnUpdate, btnDelete, btnLoad;

    // Koneksi Database
    private Connection conn;
    private PreparedStatement pst;
    private ResultSet rs;

    public MahasiswaApp() {
        // Frame Settings
        setTitle("Aplikasi Data Mahasiswa");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);

        // Komponen Input
        JLabel lblNama = new JLabel("Nama:");
        lblNama.setBounds(20, 20, 100, 20);
        add(lblNama);

        txtNama = new JTextField();
        txtNama.setBounds(120, 20, 150, 20);
        add(txtNama);

        JLabel lblNIM = new JLabel("NIM:");
        lblNIM.setBounds(20, 50, 100, 20);
        add(lblNIM);

        txtNIM = new JTextField();
        txtNIM.setBounds(120, 50, 150, 20);
        add(txtNIM);

        JLabel lblJurusan = new JLabel("Jurusan:");
        lblJurusan.setBounds(20, 80, 100, 20);
        add(lblJurusan);

        txtJurusan = new JTextField();
        txtJurusan.setBounds(120, 80, 150, 20);
        add(txtJurusan);

        JLabel lblAlamat = new JLabel("Alamat:");
        lblAlamat.setBounds(20, 110, 100, 20);
        add(lblAlamat);

        txtAlamat = new JTextField();
        txtAlamat.setBounds(120, 110, 150, 20);
        add(txtAlamat);

        // Tombol CRUD
        btnTambah = new JButton("Tambah");
        btnTambah.setBounds(300, 20, 100, 30);
        add(btnTambah);

        btnUpdate = new JButton("Update");
        btnUpdate.setBounds(300, 60, 100, 30);
        add(btnUpdate);

        btnDelete = new JButton("Delete");
        btnDelete.setBounds(300, 100, 100, 30);
        add(btnDelete);

        btnLoad = new JButton("Load Data");
        btnLoad.setBounds(300, 140, 100, 30);
        add(btnLoad);

        // Tabel
        table = new JTable();
        model = new DefaultTableModel(new String[]{"ID", "Nama", "NIM", "Jurusan", "Alamat"}, 0);
        table.setModel(model);

        JScrollPane pane = new JScrollPane(table);
        pane.setBounds(20, 180, 540, 150);
        add(pane);

        // Event Listener
        btnTambah.addActionListener(e -> tambahData());
        btnUpdate.addActionListener(e -> updateData());
        btnDelete.addActionListener(e -> deleteData());
        btnLoad.addActionListener(e -> loadData());

        // Koneksi Database
        connectDatabase();
    }

    private void connectDatabase() {
        try {
            String url = "jdbc:mysql://localhost:3306/db_mahasiswa";
            String user = "root";
            String password = ""; // Ganti jika memiliki password
            conn = DriverManager.getConnection(url, user, password);
            JOptionPane.showMessageDialog(null, "Koneksi Berhasil!");
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null, "Koneksi Gagal: " + ex.getMessage());
        }
    }

    private void tambahData() {
        try {
            String sql = "INSERT INTO data_mahasiswa(nama, nim, jurusan, alamat) VALUES (?, ?, ?, ?)";
            pst = conn.prepareStatement(sql);
            pst.setString(1, txtNama.getText());
            pst.setString(2, txtNIM.getText());
            pst.setString(3, txtJurusan.getText());
            pst.setString(4, txtAlamat.getText());
            pst.executeUpdate();
            JOptionPane.showMessageDialog(null, "Data Berhasil Ditambahkan");
            loadData();
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null, ex.getMessage());
        }
    }

    private void updateData() {
        try {
            int selectedRow = table.getSelectedRow();
            String id = model.getValueAt(selectedRow, 0).toString();

            String sql = "UPDATE data_mahasiswa SET nama=?, nim=?, jurusan=?, alamat=? WHERE id=?";
            pst = conn.prepareStatement(sql);
            pst.setString(1, txtNama.getText());
            pst.setString(2, txtNIM.getText());
            pst.setString(3, txtJurusan.getText());
            pst.setString(4, txtAlamat.getText());
            pst.setString(5, id);
            pst.executeUpdate();
            JOptionPane.showMessageDialog(null, "Data Berhasil Diupdate");
            loadData();
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null, ex.getMessage());
        }
    }

    private void deleteData() {
        try {
            int selectedRow = table.getSelectedRow();
            String id = model.getValueAt(selectedRow, 0).toString();

            String sql = "DELETE FROM data_mahasiswa WHERE id=?";
            pst = conn.prepareStatement(sql);
            pst.setString(1, id);
            pst.executeUpdate();
            JOptionPane.showMessageDialog(null, "Data Berhasil Dihapus");
            loadData();
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null, ex.getMessage());
        }
    }

    private void loadData() {
        try {
            model.setRowCount(0);
            String sql = "SELECT * FROM data_mahasiswa";
            pst = conn.prepareStatement(sql);
            rs = pst.executeQuery();
            while (rs.next()) {
                model.addRow(new Object[]{
                        rs.getInt("id"),
                        rs.getString("nama"),
                        rs.getString("nim"),
                        rs.getString("jurusan"),
                        rs.getString("alamat")
                });
            }
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null, ex.getMessage());
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new MahasiswaApp().setVisible(true);
        });
    }
}
