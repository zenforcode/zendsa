# Intro to Algorithm
 An algorithm is a procedure to accomplish a specific task. An algorithm is an idea behing any reasonble,
 computer program.
 ```
 Problem: Description of the problem
 Input: sequence of inputs
 Output: sequenece of outputs
 ```
 An *algorithm* is a procedure that takes any possible input instances and transform them to the desired output.
 For example for the sorting problem, we can specify in Rust, insertion sort.
 ```rust
 fn insertion_sort<T: Ord>(arr: &mut [T]) {
    let len = arr.len();
    for i in 1..len {
        let mut j = i;
        while j > 0 && arr[j] < arr[j - 1] {
            arr.swap(j, j - 1);
            j -= 1;
        }
    }
}

fn main() {
    let mut numbers = vec![9, 5, 1, 4, 3];
    println!("Before sorting: {:?}", numbers);
    insertion_sort(&mut numbers);
    println!("After sorting: {:?}", numbers);
}
```
Note that the algo is generic and valid also for strings as well because it is generic and works on any type that implements the Ord trait.
A good algorithm has three main properties:
- correctness: produce the right results.
- efficiency: has the right performance.
- easy to implement: things that hard to implement are also hard to prove correct and maintain.

## On Correctness

Suppose that you are an actor that has to choose different movie offers to join in. Each offer
comes with first and and day of filming. Whenever you accept a job, you must commit to being 
availbale throughout the entire period.


| Movie Title         | Start Date  | End Date  | Overlaps With |
|---------------------|------------|-----------|--------------|
| The Man from Mars  | 01/01/2025 | 01/05/2025 | - |
| Excalibur          | 02/01/2025 | 04/30/2025 | The Magician |
| The Magician       | 03/15/2025 | 06/10/2025 | Excalibur, Cyber Heist |
| Mayhem            | 05/01/2025 | 07/10/2025 | The Magician |
| Cyber Heist        | 03/01/2025 | 03/20/2025 | The Magician |
| Lost in Time       | 04/15/2025 | 05/15/2025 | The Magician, Mayhem |
| Nightfall         | 06/01/2025 | 09/01/2025 | Mayhem |
| Revenge Protocol   | 07/15/2025 | 10/15/2025 | - |
| Shadow Realm      | 08/01/2025 | 11/30/2025 | Revenge Protocol |
| The Last Prophet  | 10/01/2025 | 12/15/2025 | Shadow Realm |
| The War Within    | 11/20/2025 | 02/20/2026 | The Last Prophet |
| Frozen Truth      | 12/01/2025 | 03/01/2026 | The War Within |


So you as actor are in a position to solve a movies schedule problem.

*Problem*: Movie Schedule Problem
*Input*: A set I of n internals that overlaps 
*Output*: What is the largest subset of mutually non-overlapping intervals that can be scheduled from I?
#### First Idea: EJF
First idea: *Choose the earliest job first*. 
The first instinct might be to choose the earliest job available. However, this approach is flawed because a lengthy commitment could prevent us from considering better opportunities.

1. The first movie to start is The Man from Mars (01/01/2025 - 01/05/2025) → ✅ Accept.
2. Next available job: Excalibur (02/01/2025 - 04/30/2025) → ✅ Accept.
3. Next available job: The Magician (03/15/2025 - 06/10/2025) ❌ Conflict! (Overlaps with Excalibur)
4. Next available job: Mayhem (05/01/2025 - 07/10/2025) ❌ Conflict! (Overlaps with The Magician)
As we keep picking jobs based on the earliest start, we block ourselves from better combinations.

#### Alternative apporach: SJF
```rust
#[derive(Debug)]
struct Movie {
    title: String,
    start: String,
    end: String,
    duration: u32,
}

fn shortest_job_first(mut movies: Vec<Movie>) -> Vec<Movie> {
    // Sort movies by shortest duration first
    movies.sort_by_key(|m| m.duration);
    
    let mut selected = Vec::new();
    let mut last_end_date = "".to_string();

    for movie in movies {
        if selected.is_empty() || movie.start > last_end_date {
            last_end_date = movie.end.clone();
            selected.push(movie);
        }
    }
    selected
}

fn main() {
    let movies = vec![
        Movie { title: "The Man from Mars".to_string(), start: "2025-01-01".to_string(), end: "2025-01-05".to_string(), duration: 5 },
        Movie { title: "Cyber Heist".to_string(), start: "2025-03-01".to_string(), end: "2025-03-20".to_string(), duration: 19 },
        Movie { title: "Lost in Time".to_string(), start: "2025-04-15".to_string(), end: "2025-05-15".to_string(), duration: 30 },
        Movie { title: "Excalibur".to_string(), start: "2025-02-01".to_string(), end: "2025-04-30".to_string(), duration: 89 },
        Movie { title: "The Magician".to_string(), start: "2025-03-15".to_string(), end: "2025-06-10".to_string(), duration: 88 },
    ];
    
    let selected_movies = shortest_job_first(movies);
    println!("Selected Movies Using SJF:");
    for movie in selected_movies {
        println!("{} ({} - {})", movie.title, movie.start, movie.end);
    }
}
```
Another strategy might be the Shortest Job First (SJF) strategy means always picking the movie with the shortest duration first. While this works well in CPU scheduling, it's not a good strategy for movie selection because it ignores the impact of overlaps and might lead to missing longer but more beneficial jobs.
#### Example Using Our Movie Schedule

Step 1: Picking the shortest duration movie first

We sort the movies by duration:

1.    The Man from Mars (5 days) ✅
2.    Cyber Heist (19 days) ✅
3.    Lost in Time (30 days) ✅
4.    Revenge Protocol (92 days) ❌ (Overlaps with Lost in Time)
5.    Mayhem (70 days) ❌ (Overlaps with Lost in Time)
6.    The Magician (88 days) ❌ (Overlaps with previous jobs)
7.    Excalibur (89 days) ❌
8.    Nightfall (92 days) ❌
9.    Shadow Realm (121 days) ❌
10.    The Last Prophet (76 days) ❌
11.    The War Within (92 days) ❌
12.    Frozen Truth (91 days) ❌

We only managed to fit 3 movies before getting blocked by conflicts. *A lot of opportunitiews were lost*.

