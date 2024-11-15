import java.util.ArrayList;
import java.util.List;

public class LibraryService {
    private List<LibraryManagement> books;

    public LibraryService() {
        this.books = new ArrayList<>();
        // Adding sample books across various genres
        books.add(new LibraryManagement("Romance", "Pride and Prejudice", "Jane Austen", 3));
        books.add(new LibraryManagement("Romance", "The Notebook", "Nicholas Sparks", 2));
        books.add(new LibraryManagement("Romance", "Me Before You", "Jojo Moyes", 4));

        books.add(new LibraryManagement("Mystery", "Gone Girl", "Gillian Flynn", 3));
        books.add(new LibraryManagement("Mystery", "The Girl with the Dragon Tattoo", "Stieg Larsson", 5));
        books.add(new LibraryManagement("Mystery", "Big Little Lies", "Liane Moriarty", 4));

        books.add(new LibraryManagement("Fantasy", "The Hobbit", "J.R.R. Tolkien", 3));
        books.add(new LibraryManagement("Fantasy", "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 6));
        books.add(new LibraryManagement("Fantasy", "The Name of the Wind", "Patrick Rothfuss", 5));

        books.add(new LibraryManagement("Science Fiction", "Dune", "Frank Herbert", 4));
        books.add(new LibraryManagement("Science Fiction", "Ender's Game", "Orson Scott Card", 3));
        books.add(new LibraryManagement("Science Fiction", "The Expanse", "James S.A. Corey", 5));

        books.add(new LibraryManagement("Thriller", "The Da Vinci Code", "Dan Brown", 4));
        books.add(new LibraryManagement("Thriller", "The Girl on the Train", "Paula Hawkins", 3));
        books.add(new LibraryManagement("Thriller", "Sharp Objects", "Gillian Flynn", 2));

        books.add(new LibraryManagement("Non-fiction", "Sapiens", "Yuval Noah Harari", 5));
        books.add(new LibraryManagement("Non-fiction", "Educated", "Tara Westover", 4));
        books.add(new LibraryManagement("Non-fiction", "Becoming", "Michelle Obama", 6));
    }

    public String borrowBook(String title) {
        for (LibraryManagement book : books) {
            if (book.getTitle().equalsIgnoreCase(title)) {
                if (book.getCopies() > 0) {
                    book.setCopies(book.getCopies() - 1);
                    return "You borrowed: " + title;
                } else {
                    return "Sorry, this book is currently unavailable.";
                }
            }
        }
        return "This book is not available in the library.";
    }

    public String returnBook(String title) {
        for (LibraryManagement book : books) {
            if (book.getTitle().equalsIgnoreCase(title)) {
                book.setCopies(book.getCopies() + 1);
                return "You returned: " + title;
            }
        }
        return "This book does not belong to this library.";
    }

    public List<LibraryManagement> searchByGenre(String genre) {
        List<LibraryManagement> searchResults = new ArrayList<>();
        for (LibraryManagement book : books) {
            if (book.getCategory().equalsIgnoreCase(genre)) {
                searchResults.add(book);
            }
        }
        return searchResults;
    }

    public List<LibraryManagement> searchByAuthor(String author) {
        List<LibraryManagement> searchResults = new ArrayList<>();
        for (LibraryManagement book : books) {
            if (book.getPublisher().toLowerCase().contains(author.toLowerCase())) {
                searchResults.add(book);
            }
        }
        return searchResults;
    }

    public List<LibraryManagement> getBooks() {
        return books;
    }

    public void displayBooks() {
        if (books.isEmpty()) {
            System.out.println("No books available.");
        } else {
            for (LibraryManagement book : books) {
                System.out.println(book);
                System.out.println("------------");
            }
        }
    }
}

