args = commandArgs(trailingOnly=TRUE)
if(length(args) == 0) {
  file <- 'input_day1.txt'
} else {
    file <- args[1]}

# Read in File ------------------------------------------------------------

data <- read.csv(file, header=FALSE)

# Part One ----------------------------------------------------------------

total1 <- sum(floor(data / 3) - 2)
print(paste("Answer to Part One:", total1))

# Part Two ----------------------------------------------------------------

# Function to recursively calculate fuel needed, given a number
recursive_fuel <- function(number) {
  total = 0
  number <- floor(number / 3) - 2
  if(number <= 0){return(0)
  } else {
    total <- total + number
    total <- total + recursive_fuel(number)
  }
  return(total)
}

# Apply the function to each number, then take the sum
total2 <- sum(apply(data, MARGIN=1, FUN=recursive_fuel))

print(paste("Answer to Part Two:",total2))
