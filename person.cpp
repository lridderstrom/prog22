#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		long fib();
	private:
		int age;
		long fibi(int);
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}
"global function"
long Person::fib(){
	return fibi(age);
}
"private function"
long Person::fibi(int n){
		if (n <= 1)
			return n;
		return fibi(n-1) + fibi(n-2);
	}	



extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	long Person_fib(Person * person) {return person -> fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}