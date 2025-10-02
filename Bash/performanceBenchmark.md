# node package manager benchmark

Below is the bash script that can be exeucted from the root of the project to determine speed of installation.

It compares the speed for warm install and cold install.

---
## Warm Install

#### Definition:

A warm install is when the dependencies are already present, so the package manager mostly reuses cached packages and updates only what’s needed.

#### How it works in the script:

Leaves node_modules and lockfiles intact.

---
## Cold Install

#### Definition:

A cold install is when you install all project dependencies from scratch, without any existing node_modules folder or lockfiles.

#### How it works in the script:

```
rm -rf node_modules package-lock.json yarn.lock pnpm-lock.yaml
```


Deletes any previously installed modules and lockfiles.

Forces the package manager to download and install everything anew from the registry.

--- 

file: benchmarkPef.sh
```bash
#!/bin/bash
set -o pipefail
set -o nounset

# Default ITERATIONS=3, override with argument
ITERATIONS=${1:-3}

MANAGERS=("npm" "yarn" "pnpm")
REPORT="install_speed_report.md"
LOG_DIR="benchmark_logs"

mkdir -p "$LOG_DIR"

# Function to calculate average time from log
calculate_average() {
  local file=$1
  awk '{ total += $1; count++ } END { if (count > 0) printf "%.2f", total/count; else print "0" }' "$file"
}

# Function to calculate percentage improvement (using awk instead of bc)
calculate_improvement() {
  local base=$1
  local competitor=$2
  awk "BEGIN { if ($base > 0) printf \"%.2f\", (($base - $competitor) / $base) * 100; else print \"0\" }"
}

# Initialize report
echo "# Dependency Installation Speed Report" > "$REPORT"
echo "" >> "$REPORT"
echo "Tested with $ITERATIONS iterations per package manager." >> "$REPORT"
echo "" >> "$REPORT"

# Run benchmarks
for manager in "${MANAGERS[@]}"; do
  cold_log="$LOG_DIR/${manager}_cold.log"
  warm_log="$LOG_DIR/${manager}_warm.log"
  > "$cold_log"
  > "$warm_log"

  echo "## $manager" >> "$REPORT"

  # Cold installs
  for i in $(seq 1 $ITERATIONS); do
    rm -rf node_modules package-lock.json yarn.lock pnpm-lock.yaml
    start=$(date +%s%3N)
    if $manager install --ignore-scripts &> "$LOG_DIR/${manager}_cold_${i}.txt"; then
      end=$(date +%s%3N)
      echo $((end-start)) >> "$cold_log"
    else
      echo "Warning: $manager cold install failed on iteration $i" | tee -a "$LOG_DIR/${manager}_cold_${i}.txt"
    fi
  done

  # Warm installs
  for i in $(seq 1 $ITERATIONS); do
    start=$(date +%s%3N)
    if $manager install --ignore-scripts &> "$LOG_DIR/${manager}_warm_${i}.txt"; then
      end=$(date +%s%3N)
      echo $((end-start)) >> "$warm_log"
    else
      echo "Warning: $manager warm install failed on iteration $i" | tee -a "$LOG_DIR/${manager}_warm_${i}.txt"
    fi
  done

  cold_avg=$(calculate_average "$cold_log")
  warm_avg=$(calculate_average "$warm_log")

  echo "- Average Cold install: ${cold_avg} ms" >> "$REPORT"
  echo "- Average Warm install: ${warm_avg} ms" >> "$REPORT"
  echo "" >> "$REPORT"

  # Save results for comparisons
  declare "${manager}_cold_avg=$cold_avg"
  declare "${manager}_warm_avg=$warm_avg"
done

# Add comparison section
{
  echo "## Percentage Improvements"
  echo ""
  echo "yarn vs npm: Cold: $(calculate_improvement $npm_cold_avg $yarn_cold_avg)%, Warm: $(calculate_improvement $npm_warm_avg $yarn_warm_avg)%"
  echo "pnpm vs npm: Cold: $(calculate_improvement $npm_cold_avg $pnpm_cold_avg)%, Warm: $(calculate_improvement $npm_warm_avg $pnpm_warm_avg)%"
  echo "npm vs yarn: Cold: $(calculate_improvement $yarn_cold_avg $npm_cold_avg)%, Warm: $(calculate_improvement $yarn_warm_avg $npm_warm_avg)%"
  echo "pnpm vs yarn: Cold: $(calculate_improvement $yarn_cold_avg $pnpm_cold_avg)%, Warm: $(calculate_improvement $yarn_warm_avg $pnpm_warm_avg)%"
  echo "npm vs pnpm: Cold: $(calculate_improvement $pnpm_cold_avg $npm_cold_avg)%, Warm: $(calculate_improvement $pnpm_warm_avg $npm_warm_avg)%"
  echo "yarn vs pnpm: Cold: $(calculate_improvement $pnpm_cold_avg $yarn_cold_avg)%, Warm: $(calculate_improvement $pnpm_warm_avg $yarn_warm_avg)%"
} >> "$REPORT"

```