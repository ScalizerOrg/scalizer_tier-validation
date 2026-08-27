/** @odoo-module **/

import {
    ReviewsTable,
    reviewsTableComponent,
} from "@base_tier_validation/components/tier_review_widget/tier_review_widget.esm";
import {patch} from "@web/core/utils/patch";

reviewsTableComponent.relatedFields.push(
    {name: "constraint_type", type: "selection"},
    {name: "constraint_message", type: "text"}
);

patch(ReviewsTable.prototype, {
    _getWarningReviews() {
        return this._getReviewData().filter(
            (review) =>
                (review.status === "pending" || review.status === "waiting") &&
                review.constraint_type === "warning"
        );
    },
});
