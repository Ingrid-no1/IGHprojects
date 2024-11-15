import javax.swing.*;
import java.awt.*;
import java.util.List;

public class LibraryAppSwing {

    private JTextArea displayArea;
    private LibraryService libraryService;

    public LibraryAppSwing() {
        libraryService = new LibraryService(); // Initialize LibraryService
        initUI();
    }

    private void initUI() {
        JFrame frame = new JFrame("Library Management System");
        frame.setSize(600, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create components
        displayArea = new JTextArea();
        displayArea.setEditable(false);
        
        JButton viewBooksBtn = new JButton("View All Books");
        JButton borrowBookBtn = new JButton("Borrow a Book");
        JButton returnBookBtn = new JButton("Return a Book");
        JButton searchGenreBtn = new JButton("Search by Genre");
        JButton searchAuthorBtn = new JButton("Search by Author");

        // Set up actions for buttons
        viewBooksBtn.addActionListener(e -> displayBooks());
        borrowBookBtn.addActionListener(e -> handleBorrowBook());
        returnBookBtn.addActionListener(e -> handleReturnBook());
        searchGenreBtn.addActionListener(e -> handleSearchGenre());
        searchAuthorBtn.addActionListener(e -> handleSearchAuthor());

        // Layout
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());
        panel.add(viewBooksBtn);
        panel.add(borrowBookBtn);
        panel.add(returnBookBtn);
        panel.add(searchGenreBtn);
        panel.add(searchAuthorBtn);

        frame.add(panel, BorderLayout.NORTH);
        frame.add(new JScrollPane(displayArea), BorderLayout.CENTER);

        frame.setVisible(true);
    }

    private void displayBooks() {
        displayArea.setText("All Books:\n\n");
        for (LibraryManagement book : libraryService.getBooks()) {
            displayArea.append(book + "\n------------\n");
        }
    }

    private void handleBorrowBook() {
        String title = JOptionPane.showInputDialog("Enter the title of the book to borrow:");
        if (title != null && !title.isEmpty()) {
            String result = libraryService.borrowBook(title);
            displayArea.append(result + "\n");
        }
    }

    private void handleReturnBook() {
        String title = JOptionPane.showInputDialog("Enter the title of the book to return:");
        if (title != null && !title.isEmpty()) {
            String result = libraryService.returnBook(title);
            displayArea.append(result + "\n");
        }
    }

    private void handleSearchGenre() {
        String genre = JOptionPane.showInputDialog("Enter genre (e.g., Romance, Mystery):");
        if (genre != null && !genre.isEmpty()) {
            displayArea.setText("Books in " + genre + " genre:\n\n");
            List<LibraryManagement> genreResults = libraryService.searchByGenre(genre);
            if (genreResults.isEmpty()) {
                displayArea.append("No books found in this genre.\n");
            } else {
                genreResults.forEach(book -> displayArea.append(book + "\n------------\n"));
            }
        }
    }

    private void handleSearchAuthor() {
        String author = JOptionPane.showInputDialog("Enter the author name:");
        if (author != null && !author.isEmpty()) {
            displayArea.setText("Books by " + author + ":\n\n");
            List<LibraryManagement> authorResults = libraryService.searchByAuthor(author);
            if (authorResults.isEmpty()) {
                displayArea.append("No books found by this author.\n");
            } else {
                authorResults.forEach(book -> displayArea.append(book + "\n------------\n"));
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(LibraryAppSwing::new);
    }
}
