public class LibraryManagement {
   private String category;
   private String title;
   private String publisher;
   private int copies;
  
   public LibraryManagement(String category, String title, String publisher, int copies) {
       this.category = category;
       this.title = title;
       this.publisher = publisher;
       this.copies = copies;
   }

   public String getCategory() {
       return category;
   }

   public void setCategory(String category) {
       this.category = category;
   }

   public String getTitle() {
       return title;
   }

   public void setTitle(String title) {
       this.title = title;
   }

   public String getPublisher() {
       return publisher;
   }

   public void setPublisher(String publisher) {
       this.publisher = publisher;
   }

   public int getCopies() {
       return copies;
   }

   public void setCopies(int copies) {
       this.copies = copies;
   }

   @Override
   public String toString() {
       return "\nCategory: " + category + "\nTitle: " + title + "\nPublisher: " + publisher + "\nCopies: " + copies;
   }
}
