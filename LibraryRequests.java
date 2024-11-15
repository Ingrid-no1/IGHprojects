import java.util.List;
import java.util.Scanner;

public class LibraryRequests {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        LibraryService libraryService = new LibraryService();

        System.out.println("Welcome to the Library!");

        // Display all available books
        System.out.println("Available Books:");
        libraryService.displayBooks();

        // Main loop
        while (true) {
            System.out.println("\nChoose an option:");
            System.out.println("1. Borrow a Book");
            System.out.println("2. Return a Book");
            System.out.println("3. Search by Genre");
            System.out.println("4. Search by Author");
            System.out.println("5. Exit");

            int option = input.nextInt();
            input.nextLine();  // Consume newline

            switch (option) {
                case 1:
                    // Borrow a book
                    System.out.println("Enter the title of the book you want to borrow:");
                    String borrowTitle = input.nextLine();
                    System.out.println(libraryService.borrowBook(borrowTitle));
                    break;

                case 2:
                    // Return a book
                    System.out.println("Enter the title of the book you want to return:");
                    String returnTitle = input.nextLine();
                    System.out.println(libraryService.returnBook(returnTitle));
                    break;

                case 3:
                    // Search by genre
                    System.out.println("Choose a genre:");
                    System.out.println("1. Romance\n2. Mystery\n3. Fantasy\n4. Science Fiction\n5. Thriller\n6. Non-fiction");
                    int genreOption = input.nextInt();
                    input.nextLine();  // Consume newline
                    String genre = switch (genreOption) {
                        case 1 -> "Romance";
                        case 2 -> "Mystery";
                        case 3 -> "Fantasy";
                        case 4 -> "Science Fiction";
                        case 5 -> "Thriller";
                        case 6 -> "Non-fiction";
                        default -> "";
                    };
                    if (!genre.isEmpty()) {
                        List<LibraryManagement> genreResults = libraryService.searchByGenre(genre);
                        if (genreResults.isEmpty()) {
                            System.out.println("No books found in this genre.");
                        } else {
                            System.out.println("Books in " + genre + " genre:");
                            for (LibraryManagement book : genreResults) {
                                System.out.println(book);
                                System.out.println("------------");
                            }
                        }
                    } else {
                        System.out.println("Invalid genre option.");
                    }
                    break;

                case 4:
                    // Search by author
                    System.out.println("Enter the author name:");
                    String author = input.nextLine();
                    List<LibraryManagement> authorResults = libraryService.searchByAuthor(author);
                    
                    if (authorResults.isEmpty()) {
                        System.out.println("No books found by this author.");
                    } else {
                        System.out.println("Books by " + author + ":");
                        for (LibraryManagement book : authorResults) {
                            System.out.println(book);
                            System.out.println("------------");
                        }
                    }
                    break;

                case 5:
                    System.out.println("Exiting library system.");
                    input.close();
                    return;

                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
    }
}
